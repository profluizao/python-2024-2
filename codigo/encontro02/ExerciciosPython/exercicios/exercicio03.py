# Faça um programa usando Linguagem Python, que imprima a média aritmética de três números.
# Ao final, o programa deve imprimir os resultados dos cálculos.

# Solicita ao usuário que digite três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Calcula a soma dos números
soma = numero1 + numero2 + numero3

# Calcula a média aritmética
media = soma / 3

# Exibe os resultados
print(f"A soma dos três números é: {soma}")
print(f"A média aritmética dos três números é: {media}")
