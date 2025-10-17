# calculadora_backend.py

import math

class Backend:
    # Somar
    def somar(self, num1, num2):
        return num1 + num2

    # Subtrair
    def subtrair(self, num1, num2):
        return num1 - num2

    # Multiplicar
    def multiplicar(self, num1, num2):
        return num1 * num2

    # Dividir
    def dividir(self, num1, num2):
        if num2 == 0:
            return "Erro: Divisão por zero"
        quociente = num1 / num2
        resto = num1 % num2
        return quociente, resto

    # Potenciar
    def potencia(self, num1, num2):
        return num1 ** num2

    # Tirar a Raiz Quadrada
    def raiz_quadrada(self, num1):
        if num1 < 0:
            return "Erro: Raiz de número negativo"
        return math.sqrt(num1)

    # Bhaskara
    def bhaskara(self, a, b, c):
        delta = (b**2) - (4*a*c)
        if delta < 0:
            return "Não há raízes reais", ""
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return x1, x2