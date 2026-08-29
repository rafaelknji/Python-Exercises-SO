from modulo import fatorial, euler, sequenciaFibonacci

class Matematica:

    def fatorial(self, n):
        if(n < 0):
            raise OverflowError("O numero deve ser positivo!")
        return fatorial(n)

    def euler(self, n):
        if(n < 0):
            raise OverflowError("O numero deve ser positivo!")
        return euler(n)

    def sequenciaFibonacci(self, n):
        if(n < 0):
            raise OverflowError("O numero deve ser positivo!")
        return sequenciaFibonacci(n)