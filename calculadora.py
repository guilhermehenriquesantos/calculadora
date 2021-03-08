import math
import os

#################################################### FUNCTIONS #######################################################

def somatorio(numero_1, numero_2):
    resultado = numero_1 + numero_2
    print ("\n####################################################")
    print ("O resultado da soma entre", numero_1, "e", numero_2, "é:", resultado)
    print ("####################################################\n")

def subtracao(numero_1, numero_2):
    resultado = numero_1 - numero_2
    print ("\n####################################################")
    print ("O resultado da subtração entre", numero_1, "e", numero_2, "é:", resultado)
    print ("####################################################\n")

def multiplicacao(numero_1, numero_2):
    resultado = numero_1 * numero_2
    print ("\n####################################################")
    print ("O resultado da multiplicação entre", numero_1, "e", numero_2, "é:", resultado)
    print ("####################################################\n")

def divisao(numero_1, numero_2):
    if (numero_2 == 0):
        print ("\n##########################################")
        print ("## Não existe divisão por zero, infinito! ##")
        print ("##########################################\n")
    else:
        resultado = numero_1 / numero_2
        print ("\n####################################################")
        print ("O resultado da divisão entre", numero_1, "e", numero_2, "é: %.2f" %resultado)
        print ("####################################################\n")

def potencia(numero_1, numero_2):
    resultado = math.pow(numero_1, numero_2)
    print ("\n####################################################")
    print ("O resultado de", numero_1, "elevado à potência", numero_2, "é:", resultado)
    print ("####################################################\n")

def raiz(numero_1, numero_2):
    resultado = math.pow(numero_1, (1/numero_2))
    print ("\n####################################################")
    print ("O resultado da raiz", numero_2, "de", numero_1, "é:", resultado)
    print ("####################################################\n")

def menu():

    print("\nQual tipo de operação você irá querer realizar:\n")
    print("1 - SOMA (a + b)")
    print("2 - SUBTRAÇÃO (a - b)")
    print("3 - MULTIPLICAÇÃO (a * b)")
    print("4 - DIVISÃO (a / b)")
    print("5 - POTÊNCIA (a ^ b)")
    print("6 - RAIZ (raiz b-ésima de a)")
    print("7 - LIMPAR A TELA")
    print("8 - SAIR \n")
    opcao = int(input("Digite o número correspondente à opção que você deseja escolher: "))

    if opcao == 8:
        print ("\n#############################################\n## Qualquer coisa, só me chamar novamente! ##\n#############################################\n")
        exit()
    elif opcao >= 1 and opcao <= 6:
        realiza(opcao)
    elif opcao == 7:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
    else:
        print("\n#############################################\n## Escolha uma opção válida para operação! ##\n#############################################\n")


def realiza(operacao):
    tipo_de_numero = input("\nDigite i se deseja fazer as contas com números inteiros ou f se deseja usar números de ponto flutante: ")
    
    if tipo_de_numero == "i" or tipo_de_numero == "I":
        print("\n###############################################\n## Esta conta possui apenas números inteiros ##\n###############################################\n")
        numero_1 = int(input("Insira o primeiro numero: "))
        numero_2 = int(input("Insira o segundo numero: "))

    elif tipo_de_numero == "f" or tipo_de_numero == "F":
        print("\n#########################################################\n## Esta conta possui apenas números de ponto flutuante ##\n#########################################################\n")
        numero_1 = float(input("Insira o primeiro numero: "))
        numero_2 = float(input("Insira o segundo numero: "))
    else:
        print("\nDigite apenas i ou f\n")
        realiza(operacao)


    if operacao == 1:
        somatorio(numero_1, numero_2)
    elif operacao == 2:
        subtracao(numero_1, numero_2)
    elif operacao == 3:
        multiplicacao(numero_1, numero_2)
    elif operacao == 4:
        divisao(numero_1, numero_2)
    elif operacao == 5:
        potencia(numero_1, numero_2)
    elif operacao == 6:
        raiz(numero_1, numero_2)
    else:
        print("\nEscolha uma opção válida para operação!\n")
    
    menu()


###################################################### MAIN ####################################################

print("\n########################### CALCULADORA MATEMÁTICA BÁSICA ###########################\n")

menu()

exit()