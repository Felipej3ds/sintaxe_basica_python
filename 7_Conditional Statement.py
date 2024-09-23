"""tipos de estruturas de repetição em python
Python If else
Nested if statement
Python if-elif-else Ladder
Python If Else on One Line
Ternary Condition in Python
Match Case Statement
"""
#if: execulta ou não um bloco de comandos caso a condição seja verdadeira
i = 10

if i == 10:
    print("a condições é verdadeira")

#if/else:

i = 10

if i > 10:
    print("o numero é maior que 10")
else:
    print("o numero não é maior que 10")

#nested if statement
"""
um if...elif...else dentro de outro if...elif...else

"""
i = 0; 
if i != 0:
    if i > 0:
        print("Positive")
    if i < 0:
        print("Negative")
else:
    print("Zero")



#elif
i = 25
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")  


#if else em uma linha utilizando o metodo get()

x = 0

resultado = {x > 0: "positivo", x < 0: "negativo"}.get(True,"zero")
print(resultado)

#match case
i = 0
match i:
    case 1:
        print("é um")
    case 2:
        print("é dois")
    case 3:
        print('é tres')
    case 0:
        print("é zero")


#operador ternario

a = 20
b = 30

min = "a é o maior numero" if a > b else "b é o maior numero"

print("a e b são iguais" if a == b else "a é o maior numero" if a > b else "b é maior")

print(("a é maior que b", "b é maior que a") [a < b])

print({True: "b é maior que a", False: "a é maior que b"} [b > a])

print((lambda: "b > a", lambda: "a > b") [b < a]())

