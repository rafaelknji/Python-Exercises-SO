## Modifique o programa de VALOR para usar lock e acquire

import threading

VALOR = 0
lock = threading.Lock()

def somar():
    global VALOR
    lock.acquire()
    VALOR += 10
    lock.release()

def diminuir():
    global VALOR
    lock.acquire()
    VALOR -= 10
    lock.release()

threads = []

for i in range(500):
    t1 = threading.Thread(target=somar)
    t2 = threading.Thread(target=diminuir)

    threads.append(t1)
    threads.append(t2)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Valor final:", VALOR)
