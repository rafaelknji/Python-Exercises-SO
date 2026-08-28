#Conte quantos números primos menores que 1.000.000.000 existem.

def numeroPrimo(numero):
    resto0 = 0
    for i in range (1, numero+1):
       if numero % i == 0:
           resto0 = resto0+1

    if resto0 == 2:
        return True
    else:
        return False


numerosTotais = 0
numerosPrimos = []

for i in range(1, 1000000000):
    print(i)
    if numeroPrimo(i) == True:
        numerosTotais += 1
        numerosPrimos.append(i)

print("Quantidade total = ", numerosTotais)
