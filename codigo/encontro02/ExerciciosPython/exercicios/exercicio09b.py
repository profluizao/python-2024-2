# Desenvolva um programa em Python que leia uma lista de 5 nomes fornecidos pelo usuário e conte
# quantos desses nomes contêm a letra 'a' (maiúscula ou minúscula).
# O programa deve usar a instrução while para percorrer a lista e realizar a contagem.

# Cria uma lista vazia para armazenar os nomes
nomes = []

# Solicita ao usuário que insira 5 nomes
print("Digite 5 nomes:")
i = 0
while i < 5:
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)
    i += 1

# Conta quantos nomes contêm a letra 'a' (ou 'A')
contador = 0
indice = 0
while indice < len(nomes):
    nome = nomes[indice]
    if 'a' in nome.lower():  # Verifica se a letra 'a' está no nome, ignorando maiúsculas e minúsculas
        contador += 1
    indice += 1

# Imprime o número de nomes que contêm a letra 'a'
print(f"Número de nomes que contêm a letra 'a': {contador}")
