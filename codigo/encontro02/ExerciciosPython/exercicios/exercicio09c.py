# Desenvolva um programa em Python que leia números inteiros fornecidos pelo usuário e
# calcule a soma de todos os números positivos inseridos. O programa deve usar a instrução while
# para continuar lendo números até que o usuário insira um número negativo.
# O programa deve, então, imprimir a soma dos números positivos.

# Inicializa a variável de soma
soma_positivos = 0

# Solicita ao usuário que insira números inteiros até que um número negativo seja inserido
while True:
    numero = int(input("Digite um número inteiro (ou um número negativo para terminar): "))

    # Verifica se o número é negativo para terminar o loop
    if numero < 0:
        break

    # Adiciona o número positivo à soma
    soma_positivos += numero

# Imprime a soma dos números positivos
print(f"Soma dos números positivos: {soma_positivos}")
