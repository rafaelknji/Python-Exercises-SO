
import threading

VALOR = 0

def somar():
    global VALOR
    VALOR += 10

def diminuir():
    global VALOR
    VALOR -= 10

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
