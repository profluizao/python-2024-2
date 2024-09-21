# Desenvolver um programa em Linguagem Python, que leia um número inteiro e verifique se o número é divisível
# por 5 e por 3 ao mesmo tempo.

# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 5 e por 3
if numero % 5 == 0 and numero % 3 == 0:
    print(f"O número {numero} é divisível por 5 e por 3 ao mesmo tempo.")
else:
    print(f"O número {numero} não é divisível por 5 e por 3 ao mesmo tempo.")
