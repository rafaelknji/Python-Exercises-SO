# Crie um programa que use uma variável global chamada VALOR que é acessada por mil threads
# 500 threads somam 10 em VALOR
# 500 threads diminuem 10 em VALOR
# - Rode sem usar sleep Exiba VALOR ao final 

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
