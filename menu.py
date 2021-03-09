# Criando um menu interativo

print ("\nEscolha uma reação que represente o que você está sentindo agora:\n")
print ("1 - Curtir")
print ("2 - Amei")
print ("3 - Força")
print ("4 - Haha")
print ("5 - Uau")
print ("6 - Triste")
print ("7 - Grr\n")

opcao = input("Digite o NÚMERO que te represente neste momento: ")

if opcao == '1':
    print('\n#################################')
    print('# Você está curtindo o momento! #')
    print('#################################\n')
elif opcao == '2':
    print('\n###############################')
    print('# Você está amando o momento! #')
    print('###############################\n')
elif opcao == '3':
    print('\n#########################')
    print('# Muita força pra você! #')
    print('#########################\n')
elif opcao == '4':
    print('\n###########################')
    print('# Você é muito engraçado! #')
    print('###########################\n')
elif opcao == '5':
    print('\n########################')
    print('# Tá impressionado né? #')
    print('########################\n')
elif opcao == '6':
    print('\n#######################################')
    print('# Não fica triste não, tu é incrível! #')
    print('#######################################\n')
elif opcao == '7':
    print('\n############################')
    print('# Dá logo um socão ksksksk #')
    print('############################\n')
else:
    print('\n#############################')
    print('# Escolha uma opção válida! #')
    print('#############################\n')