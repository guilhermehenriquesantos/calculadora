# APRENDENDO A USAR O MATH
import math

# Descobrindo a potência de um número

# 2²
dois_ao_quadrado = math.pow(2, 2)
print("\n")
print ("Dois elevado ao quadrado:", dois_ao_quadrado)
print("\n")

# 6⁰
seis_elevado_a_zero = math.pow(6, 0)
print ("Seis elevado à zero:", seis_elevado_a_zero)
print("\n")

# 4⁵
quatro_elevado_a_cinco = math.pow(4, 5)
print ("Quatro elevado à quinta:", quatro_elevado_a_cinco)
print("\n")

# 1⁹⁸
um_elevado_a_noventa_e_oito = math.pow(1, 98)
print ("Um elevado à noventa e oito:", um_elevado_a_noventa_e_oito)
print("\n")

# Tirando raiz n-ésima de um número
raiz_quadrada_de_vinte_e_cinco = math.pow(25, (1/2))
print ("A raiz quadrada de vinte e cinco é:", raiz_quadrada_de_vinte_e_cinco)
print("\n")

raiz_cubica_de_vinte_e_sete = math.pow(27, (1/3))
print ("A raiz cúbica de vinte e sete é:", raiz_cubica_de_vinte_e_sete)
print("\n")

raiz_quarta_de_dezesseis = math.pow(16, (1/4))
print ("A raiz quarta de dezesseis é:", raiz_quarta_de_dezesseis)
print("\n")

#################################################

# Com entrada do usário - potência:
base = int(input("\nDigite um valor inteiro para a base: "))
expoente = int(input("Digite um valor inteiro para o expoente: "))
potencia = math.pow(base, expoente)
print (base, "elevado à", expoente, "=", potencia, "\n")

# Com entrada do usário - raiz:
base = int(input("\nDigite um valor inteiro para a base: "))
raiz = int(input("Digite um valor inteiro para representar a raiz: "))
resultado = math.pow(base, (1/raiz))
print ("raiz", raiz, "de", base, "=", resultado, "\n")