from Matematica import Matematica

mat = Matematica()

while True:
    print("\n========MENU========")
    print("1 - Fatorial")
    print("2 - Fibonacci")
    print("3 - Euler")
    print("0 - Sair")

    opcao = int(input("Digite uma opcao: "))


    try:
        match opcao:
            case 1:
                n = int(input("\nQual numero deseja calcular? "))
                print(f"{n}! = {mat.fatorial(n)}")
            case 2:
                n = int(input("Digite o limite da sequência de Fibonacci: "))
                fibonacci, soma = mat.sequenciaFibonacci(n)
                print("\nSequencia Fibonacci =",fibonacci)
            case 3:
                n = int(input("\nDigite o limite de Euler: "))
                mat.euler(n)
            case 0:
                break
            case _:
                print("Opcao invalida!")
    except OverflowError as erro:
        print(erro)