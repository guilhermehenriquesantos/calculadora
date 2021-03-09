# Limpando a tela do sistema
import os

# Loop infinito enquanto não atender o requisito de saída
while(True):
    print("\nEscrevendo na tela do usuário")

    var = input('\nDeseja limpar a tela? Digite S se sim: ')

    if var == "S" or var == "s" or var == "Sim" or var == "sim" or var == "SIM":
        # Se for windows aplicar o comando cls no cmd, se for linux aplicar o comando clear no terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    sair = input('\nDeseja sair? Digite S se sim: ')

    if sair == "S" or sair == "s" or sair == "Sim" or sair == "sim" or sair == "SIM":
        # Parando um laço
        break
