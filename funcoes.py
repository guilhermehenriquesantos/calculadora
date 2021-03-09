# FUNÇÕES EM PYTHON #
#####################

# Quando eu preciso de uma função? 
# Resposta: sempre que vou repetir uma ação mais de uma vez é vantajoso utilizar das funções para isso, 
# pois assim, você programa uma vez só e apenas a chama quando precisar de executar tal função, exemplo:

# Quero somar e multiplicar 3 números, após isso quero printar a subtração dos resultados na tela do usuário
def soma_e_multiplica_tres_numeros(numero_1, numero_2, numero_3):
    soma = numero_1 + numero_2 + numero_3
    multiplicacao = numero_1 * numero_2 * numero_3

    resultado = multiplicacao - soma

    print("\n#######################################################################################")
    print("A soma dos números:", numero_1, numero_2, numero_3, "é:", soma)
    print("A multiplicação dos números:", numero_1, numero_2, numero_3, "é:", multiplicacao)
    print("O resultado de multiplicação - soma é:", resultado)
    print("#######################################################################################\n")


# PROGRAMA PRINCIPAL

# Chamando funções
soma_e_multiplica_tres_numeros(1, 2, 3)
soma_e_multiplica_tres_numeros(5, 8, 7)
soma_e_multiplica_tres_numeros(10, 11, 200)

# Pedindo para o usuário digitar e colocar nas funções
primeiro_numero = int(input("Digite o primeiro número inteiro: "))
segundo_numero = int(input("Digite o segundo número inteiro: "))
terceiro_numero = int(input("Digite o terceiro número inteiro: "))

soma_e_multiplica_tres_numeros(primeiro_numero, segundo_numero, terceiro_numero)