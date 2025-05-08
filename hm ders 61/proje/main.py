import socket
import threading
import json
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
clients = {}
lock = threading.Lock()
LOG_FILE = "chat_server.log"

def log_event(event_type, details):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "details": details
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def broadcast(message, sender=None):
    with lock:
        for client, info in clients.items():
            if client != sender:
                try:
                    client.send(message.encode(encoding='utf-8'))
                except:
                    log_event("client_disconnect_error",
                              {"client": info['username']})
                    del clients[client]

def handle_client(conn, addr):
    try:
        username = conn.recv(1024).decode()
        with lock:
            clients[conn] = {
                "username":username,
                "ip": addr[0],
                "join_time": datetime.now().isoformat()
            }
            log_event("user_joined", {"username": username, "ip": addr[0]})
            broadcast(f"{username} sohbete katıldı!", sender=conn)
            while True:
                message = conn.recv(1024).decode()
                if not message or message.lower() == 'quit':
                    break
                log_event("message_received", {
                    "username": username,
                    "message": message
                })
                broadcast(f"{username}: {message}", sender=conn)
    except Exception as e:
        log_event("client_error", {"error": str(e), "ip": addr[0]})
    finally:
        with lock:
            if conn in clients:
                username = clients[conn]["username"]
                broadcast(f"{username} sohbetten ayrıldı", sender=conn)
                log_event("user_left", {"username": username})
                del clients[conn]
                conn.close()

def start_chat_server():
    host='0.0.0.0'
    port = 55555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    log_event("server_start", {"host": host, "port": port})
    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    except KeyboardInterrupt:
        log_event("server_shutdown", {"reason": "keyboard_interrupt"})
    finally:
        server.close()

@app.route('/status', methods=['GET'])
def get_status():
    with lock:
        client_list = [{
            "username": info["username"],
            "ip": info["ip"],
            "join_time": info["join_time"]
        } for _, info in clients.items()]
        log_event("status_check", {"client_count": len(client_list)})
        return jsonify({
            "status": "running",
            "clients": client_list,
            "client_count": len(client_list),
            "timestamp": datetime.now().isoformat()
        })
    
@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        with open(LOG_FILE, "r") as f:
            logs = [json.loads(line) for line in f.readlines()]
            return jsonify({"logs": logs})
    except FileNotFoundError:
        return jsonify({"error": "Log file not found"}), 404
    
if __name__ == "__main__":
    server_thread = threading.Thread(target=start_chat_server)
    server_thread.daemon = True
    server_thread.start()
    app.run(port=5000, debug=False)
    
