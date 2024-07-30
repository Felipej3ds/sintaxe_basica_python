"""objetivo
entrada de dados
  - input(): sempre produz um dado do tipo string
"""

print(input(" digite a idade: "))

a = input("digite um nome: ")
print(a)

print("seu nome é: {}".format(a))

try: 

    altura = float(input("digite a altura: "))
    print(f"a altura digitada é: {altura}")

    print(type(altura))
except:
    print("altura não é valida")
