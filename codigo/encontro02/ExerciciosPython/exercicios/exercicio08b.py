# Crie um programa em Linguagem Python, que leia 5 números (utilizando arrays) e mostre o dobro,
# o triplo e a raiz quadrada de cada um.
# Utilize a instrução for para exibir os dados.

import math  # Biblioteca para cálculo da raiz quadrada

# Cria uma lista (array) vazia para armazenar os números
numeros = []

# Solicita ao usuário que insira 5 números
for i in range(5):
    numero = float(input(f"Digite o número { i +1}: "))
    numeros.append(numero)

# Exibe o dobro, o triplo e a raiz quadrada de cada número
print("\nResultados:")
for numero in numeros:
    dobro = numero * 2
    triplo = numero * 3
    raiz_quadrada = math.sqrt(numero)

    print(f"Para o número {numero}:")
    print(f"Dobro: {dobro}")
    print(f"Triplo: {triplo}")
    print(f"Raiz Quadrada: {raiz_quadrada:.2f}\n")  # Formata a raiz quadrada com 2 casas decimais
