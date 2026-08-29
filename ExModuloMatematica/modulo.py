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
    return fibonacci, soma


def euler(limite):
    resultados = []
    for n in range(1, limite+1):
        euler = (n*n) - n + 41
        print(n, "*", n, "-", n, "+ 41 = ", euler)
        resultados.append(euler)
    return resultados


def fatorial(n):
    resultado = n
    for i in range(n-1, 0, -1):
        resultado *= i  
    return resultado




