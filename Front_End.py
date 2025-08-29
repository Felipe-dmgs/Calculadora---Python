from Time import sleep
class frontend():
    def iniciarPrograma():
        print("Iniciando a Calculadora");
        for i in range(10):
            print(".\n");
            sleep(0.3);
        print("Calculadora Iniciada");
        escolha = int(input("Qual operação deseja realizar??\n Soma[1]\n Subtração[2]\n Multiplicação[3]\n Divisão[4]\n Potência[5]\n Raiz[6]\n Baskara[7]\n Fechar a calculadora[0]"))
        return escolha
    def resultado(valor):
        print(f"O resultado da sua conta é {valor}");
    def fecharPrograma():
        print("Calculadora fechada!!")