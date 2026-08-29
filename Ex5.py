# Use a fórmula de Euler n*n -n +41 para gerar números, sendo n=1 a 1000, quantos são primos?

def numeroPrimo(numero):
    resto0 = 0
    for i in range (1, numero+1):
       if numero % i == 0:
           resto0 = resto0+1

    if resto0 == 2:
        return True
    else:
        return False

qtdPrimos = 0

for n in range(1, 1001):
    euler = (n*n) - n + 41
    print(n, "*", n, "-", n, "+ 41 = ", euler)

    if numeroPrimo(euler) == True:
        qtdPrimos += 1
print("\nQuantidade de N Primos: ", qtdPrimos)
