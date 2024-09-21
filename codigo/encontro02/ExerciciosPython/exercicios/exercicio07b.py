# Desenvolva um programa em Python que leia a nota final de um aluno e determine sua situação acadêmica com base na seguinte tabela:
# - Nota >= 7: Aprovado
# - Nota >= 5 e < 7: Em Recuperação
# - Nota < 5: Reprovado

# Solicita ao usuário que digite a nota final do aluno
nota = float(input("Digite a nota final do aluno: "))

# Determina a situação acadêmica com base na nota
if nota >= 7:
    situacao = "Aprovado"
elif 5 <= nota < 7:
    situacao = "Em Recuperação"
else:
    situacao = "Reprovado"

# Imprime a situação acadêmica
print(f"Situação Acadêmica: {situacao}")

