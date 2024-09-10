#Algumas palavras na linguagem são reservadas, possuem significado própio, e não podem ser reutilizadas

# while - Estrutura de repetição enquanto uma condição é verdadeira
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# yield - Utilizado em funções geradoras para retornar um valor sem encerrar a função
def gerador():
    yield 1
    yield 2
    yield 3

gen = gerador()
print(next(gen)) 
'''Saída: 1'''

# async, await - Usado para definir funções assíncronas e esperar o resultado de uma coroutine
import asyncio

async def async_function():
    await asyncio.sleep(1)
    return 'feito!'

async def main():
    print(await async_function())

asyncio.run(main())

# and - Operador lógico AND
x = True
y = False
print(x and y)  

# assert - Checa se uma condição é verdadeira, caso contrário, levanta uma exceção AssertionError
x1 = 5
assert x == 5, "O valor de x não é 5"

# break - Sai de um loop
for i in range(10):
    print(i)
    if i == 5:
        break

# class - Define uma classe
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

# continue - Pula a iteração atual de um loop e continua para a próxima
for i in range(5):
    if i == 3:
        continue
    print(i)

# def - Define uma função
def soma(a, b):
    return a + b

print(soma(3, 4))  
"Saída: 7 "


# del - Remove u ma variável, item de uma lista, atributo de um objeto, etc.
x2 = 5
del x

# elif - Condicional "else if" usado em estruturas condicionais
x3 = 10
if x3 < 5:
    print("Menor que 5")
elif x3 == 5:
    print("Igual a 5")
else:
    print("Maior que 5")

# else - Bloco executado quando a condição de um if não é satisfeita
x3 = 5
if x3 > 0:
    print("x é positivo")
else:
    print("x não é positivo")

# except - Captura exceções em blocos try-except
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro de divisão por zero")

# finally - Bloco que é sempre executado ao final de um bloco try-except, independentemente de exceções
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro de divisão por zero")
finally:
    print("Finalizando operação")

# False - Valor booleano falso
x = False

# for - Loop usado para iterar sobre uma sequência
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# from - Usado para importar partes específicas de um módulo
from math import sqrt
print(sqrt(16))  # Saída: 4.0

# global - Declara uma variável global dentro de uma função
def funcao():
    global x
    x = 10

funcao()
print(x)  # Saída: 10

# if - Estrutura condicional
x3 = 5
if x > 0:
    print("x é positivo")

# import - Importa um módulo ou pacote
import math
print(math.sqrt(16))  # Saída: 4.0

# in - Verifica se um valor está presente em uma sequência
frutas = ["maçã", "banana", "laranja"]
if "banana" in frutas:
    print("banana está na lista")

# is - Verifica se dois objetos são o mesmo objeto na memória
x4 = [1, 2, 3]
y = x
print(x is y)  # Saída: True

# lambda - Cria uma função anônima (função lambda)
dobro = lambda x: x * 2
print(dobro(4))  # Saída: 8

# nonlocal - Usado em funções aninhadas para indicar que uma variável não é local, mas também não é global
def externa():
    x = 10
    def interna():
        nonlocal x
        x = 20
    interna()
    print(x)

externa()  # Saída: 20

# not - Operador lógico NOT
x = True
print(not x)  # Saída: False

# or - Operador lógico OR
x = True
y = False
print(x or y)  # Saída: True

# pass - Palavra reservada que não faz nada, usada quando a sintaxe exige um comando
def funcao_vazia():
    pass

# raise - Levanta uma exceção explicitamente
x5 = 10
if x > 5:
    raise Exception("x não pode ser maior que 5")

# return - Retorna um valor de uma função
def soma1(a: int, b: int) -> int:
    return a + b

resultado = soma(3, 4)
print("A soma é:", resultado)  # Saída: A soma é: 7

# True - Valor booleano verdadeiro
x = True

# try - Bloco usado para exceções que pode potencialmente levantar uma exceção
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro de divisão por zero")
