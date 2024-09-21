# Desenvolva um programa em Python que leia a idade de uma pessoa e determine a categoria etária dela com base na seguinte tabela:
# - Menor de 13 anos: Criança
# - Entre 13 e 19 anos: Adolescente
# - Entre 20 e 64 anos: Adulto
# - 65 anos ou mais: Idoso

# Solicita ao usuário que digite a idade
idade = int(input("Digite sua idade: "))

# Determina a categoria etária com base na idade
if idade < 13:
    categoria = "Criança"
elif 13 <= idade <= 19:
    categoria = "Adolescente"
elif 20 <= idade <= 64:
    categoria = "Adulto"
else:
    categoria = "Idoso"

# Imprime a categoria etária
print(f"Categoria etária: {categoria}")
