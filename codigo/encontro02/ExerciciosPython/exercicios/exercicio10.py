# Faça um programa que leia o preço de um produto. Se o valor do produto for inferior à R$ 100,00,
# recalcule seu valor com 5% de desconto. Caso contrário, recalcule seu valor com 10% de desconto.
# Imprima seu novo preço, informando o valor de desconto.

# Solicita ao usuário que insira o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Verifica o valor do produto e aplica o desconto correspondente
if preco < 100:
    desconto = 0.05  # 5% de desconto
    valor_desconto = preco * desconto
    novo_preco = preco - valor_desconto
else:
    desconto = 0.10  # 10% de desconto
    valor_desconto = preco * desconto
    novo_preco = preco - valor_desconto

# Imprime o novo preço e o valor do desconto
print(f"\nPreço original: R$ {preco:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Novo preço: R$ {novo_preco:.2f}")
