# Desenvolva um programa em Python que leia uma lista de 10 números inteiros fornecidos pelo usuário e
# calcule a soma de todos os números pares presentes na lista. O programa deve usar a instrução for para
# percorrer a lista e realizar o cálculo.

# Para tanto, siga este passo a passo:
# - O programa deve solicitar ao usuário que insira 10 números inteiros.
# - O programa deve utilizar um loop for para percorrer a lista de números.
# - O programa deve calcular a soma apenas dos números pares.
# - O programa deve imprimir a soma dos números pares.

# Cria uma lista vazia para armazenar os números
numeros = []

# Solicita ao usuário que insira 10 números inteiros
print("Digite 10 números inteiros:")
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

# Calcula a soma dos números pares
soma_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero

# Imprime a soma dos números pares
print(f"A soma dos números pares é: {soma_pares}")
