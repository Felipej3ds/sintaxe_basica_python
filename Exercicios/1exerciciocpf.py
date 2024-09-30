import re, random

cpf = ''

while True:
    
    cpf = input("digite um cpf: ")

    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0]*len(cpf):
        print("Digite um CPF válido")
        continue

    soma = 0
    contador = 10

    # Calcula o primeiro dígito verificador
    for numero in cpf[:-2]:  # Ignora os últimos dois dígitos
        soma += int(numero) * contador
        contador -= 1

    primeiro_digito = (soma * 10) % 11
    if primeiro_digito > 9:
        primeiro_digito = 0

    soma = 0
    contador = 11

    for numero in cpf[:-1]:  # Ignora o último dígito
        soma += int(numero) * contador
        contador -= 1

    segundo_digito = (soma * 10) % 11
    if segundo_digito >= 10:
        segundo_digito = 0

    # Correção na montagem do CPF verificador
    cpf_verificador = f"{cpf[:9]}{primeiro_digito}{segundo_digito}"

    if cpf_verificador == cpf:
        print("CPF válido")
        break
    else:
        print("CPF inválido")
