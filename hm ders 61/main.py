import threading    
import time

def görev(isim):
    print(f"{isim} görev başlandı")
    time.sleep(2)
    print(f"{isim}görev tamamlandı")

t1 = threading.Thread(target=görev, args=("Görev 1,",))
t2 = threading.Thread(target=görev, args=("Görev 2,",))

t1.start()
t2.start()

t1.join()

t2.join()