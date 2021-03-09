# Laços

# Laço for: sempre que preciso de executar uma tarefa por determinadas vezes eu posso usar o for
# por exemplo, eu quero imprimir uma mensagem 5 vezes na tela, para isso eu faço:
for indicador in range(0, 5):
    print("Enviando mensagem:", indicador)

# Também posso usar o laço while (enquanto), ou seja, enquanto uma condição não for satisfeita ele continua rodando
# Por exemplo, enquanto o meu contador não chegar até 10, ele continuará imprimindo para mim e incrementando o valor de contador
contador = 0
while contador <= 10:
    print(contador)
    contador = contador + 1

# Outra forma de sair de um laço é fazendo um "break", aí ele sai do laço, vamos ver novamente, eu zerei contador aqui novamente
# Para podermos fazer o mesmo laço que está alí acima
contador = 0
while contador <= 10:
    print("\nNovo contador:", contador)
    contador = contador + 1
    break

print ("O valor final de contador vai ser %i, pois ele faz a conta e sai do laço" %contador)

# O break serve tanto para while quanto para o laço for.