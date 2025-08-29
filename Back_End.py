class backend():
    #Somar
    def somar(*numeros):
        total = 0
        for num in numeros:
            total += num
        return total # A soma dos seus números é X se a pessoa colocar 0 o while acaba e da o resultado
    #Subtrair
    def subtrair(*numeros):
        total = 0
        for num in numeros:
            total -= num
        return total# A subtração dos seus números é Y se a pessoa colocar 0 printa o resultado
    #Multiplicar
    def multiplicar(num1,num2):
        return num1*num2# A multiplicação dos seus números é Z, emite o resultado
    #Dividir
    def dividir(num1,num2):
        resp = [num1/num2,num1%num2]
        return resp
    #Potenciar
    def potencia(num1,num2):
        return num1**num2
    #Tirar a Raiz
    def raiz(num1,num2):
        return num1*0.5
    #baskara 
    def baskara(A,B,C):
        resp = [(-B + (((B**2) - (4*A*C))**0.5))/(2*A), (- B - (((B**2) - (4*A*C))**0.5))/2*A]
