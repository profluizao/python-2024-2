# Elabore um programa em Python, que calcule e imprima a tabuada de qualquer número informado,
# utilizando a instrução while.

# Solicita ao usuário que digite um número
numero = int(input("Digite um número para calcular a tabuada: "))

# Inicializa a variável de controle do loop
i = 1

# Calcula e imprime a tabuada do número informado
print(f"\nTabuada do {numero}:")
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1
