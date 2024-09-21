# Faça um programa usando Linguagem Python, que leia um número inteiro e imprima o seu antecessor e o seu sucessor.

# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Calcula o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1

# Exibe o antecessor e o sucessor
print(f"O antecessor de {numero} é {antecessor}.")
print(f"O sucessor de {numero} é {sucessor}.")
