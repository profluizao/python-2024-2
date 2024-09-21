# Desenvolver um programa em Linguagem Python, que leia um número x, calcule e imprima o valor de y,
# de acordo com as condições abaixo:
# y = x , se x < 1;
# y = 0 , se x = 1;
# y = x² , se x > 1;

# Solicita ao usuário que digite um número x
x = float(input("Digite o valor de x: "))

# Verifica as condições para calcular o valor de y
if x < 1:
    y = x
elif x == 1:
    y = 0
else:
    y = x ** 2  # Eleva x ao quadrado se x > 1

# Exibe o valor de y
print(f"O valor de y é: {y}")
