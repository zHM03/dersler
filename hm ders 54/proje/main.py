from collections import defaultdict

class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.connections = defaultdict(list)
        
    def add_user(self, user_id, name, surname, username):
        self.users[user_id] = {"name": name, "surname": surname, "username": username}
        
    def add_connection(self, user1, user2):
        self.connections[user1].append(user2)
        self.connections[user2].append(user1)
        
    def update_user(self, user_id, name=None, surname=None, username=None):
        if user_id in self.users:
            if name:
                self.users[user_id]["name"] = name
            if surname:
                self.users[user_id]["surname"] = surname
            if username:
                self.users[user_id]["username"] = username
        else:
            print("Kullanıcı bulunamadı!")
    
    def view_connections(self, user_id):
        if user_id in self.users:
            print(f"{self.users[user_id]['name']} {self.users[user_id]['surname']} Bağlantıları:")
            for connection in self.connections[user_id]:
                print(f"{self.users[connection]['name']} {self.users[connection]['surname']}")
        else:
            print("Kullanıcı bulunamadı")

# Testing the code
sn = SocialNetwork()
sn.add_user(1, "Mete", "wadsa", "gmakw")
sn.add_user(2, "sakror", "sopar", "awohda")
sn.add_user(3, "awdlüğas", "üawğdmas", "wadas")
sn.add_connection(1, 2)
sn.add_connection(1, 3)
sn.view_connections(1)
sn.view_connections(2)
sn.view_connections(3)
