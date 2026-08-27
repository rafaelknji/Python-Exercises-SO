# Crie uma função que determine se um número é primo ou não. Retorne True ou False.

def numeroPrimo(numero):
    resto0 = 0
    for i in range (1, numero+1):
       if numero % i == 0:
           resto0 = resto0+1

    if resto0 == 2:
        return True
    else:
        return False


numero = int(input("Digite um numero: "))
if numeroPrimo(numero) == True:
    print(f"O numero {numero} é primo!")
else:
    print(f"O numero {numero} NAO é primo!")
