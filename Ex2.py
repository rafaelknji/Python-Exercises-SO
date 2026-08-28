#Exiba na tela os números menores que 1.000.000.000 que são divididos por 13, 23 e 41 ao mesmo tempo. Mostre também quantos números você achou.

numeros = []
totalNumeros = 0

for i in range(1, 100000):
    print(i)
    if i%13==0 and i%23==0 and  i%41==0 :
        numeros.append(i)
        totalNumeros += 1

print("\nResultado = ", *numeros)
print("Quantidade total = ", totalNumeros)
