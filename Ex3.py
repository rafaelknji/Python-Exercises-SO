#Crie uma função que calcule os números da sequencia de Fibonacci. Quantos números de Fibonacci menores que 1.000.000 existem e qual a soma deles.

def sequenciaFibonacci(limite):
    fibonacci = [0, 1]

    i=2
    soma = 1

    while True:
        resultado = fibonacci[i-2] + fibonacci[i-1]

        if resultado >= limite:
            break

        print(fibonacci[i-2], " + ", fibonacci[i-1], " = " , resultado)
        fibonacci.append(resultado)
        soma += resultado
        i+=1

    print("Soma: ", soma)
    print("Quantidade: ", len(fibonacci))

sequenciaFibonacci(1000000000)