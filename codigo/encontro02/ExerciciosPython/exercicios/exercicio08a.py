# Elabore um programa em Python, que calcule e imprima a tabuada de qualquer número informado,
# utilizando a instrução for.

# Solicita ao usuário que digite um número
numero = int(input("Digite um número para calcular a tabuada: "))

# Calcula e imprime a tabuada do número informado
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
