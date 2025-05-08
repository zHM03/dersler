import threading
import time
sayac=0
kilit = threading.Lock()

def artir():
    global sayac
    with kilit:
        mevcut_deger = sayac
        mevcut_deger+=1
        time.sleep(0.1)

        sayac = mevcut_deger
threads = []
for _ in range(10):
    t = threading.Thread(target=artir)
    threads.append(t)
    t.start()

for t in threads:
    t.join