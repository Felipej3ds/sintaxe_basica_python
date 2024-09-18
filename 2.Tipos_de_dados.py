#data type é um conceito importante em qualquer linguagem de programação para armazenamento e manipulação de dados
#A lingem python por padrão possui os seguintes tipos de dados 
"""
1. tipo numerico: {int, float, complex}
2. tipo sequencial: {list, tuple, range, strg}
tipo de dicionario: dics
tipo de conjunto: {set, frozenset}
tipo booleano: {bool}
tipos binarios:{bytes, bytearray, memoryview} 
"""

#os tipos de dados ditam quais operações podem ser performadas com uma variavel
#em python os tipos de dados são classes e as variaveis são instâncias da classe

#obs: podemos saber o tipo de dado de qualquer variavel utilizando o type()

"""1º tipo de dado numerico
são dados que possuem valores numericos, podem ser valores:
inteiros(int)
flutuante(float)
complexos: (complex)
"""

int = 2 #contem numeros positivos ou negativos inteiros, sem frações
float = 2.2 #numeros representados pela classe float, e consiste de um numero real de ponto flutuante
complex = 3 + 2j #numero representado pela classe complex, (real) + (imaginario)j

"""2º tipos sequenciais
um tipo de dados que permite armazenar dados do mesmo tipo ou de tipos diferentes de maneira ordenada, são:
strings:
list:
tuple: 
"""
#string
string1 = "meu nome" #em python uma string é uma sequecia de characteres unicode
string2 = """oi 
             meu nome é
             juao
        """
#podemos acessar caracteres específicos utilizando identação
print(string2[0])# acessando o primeiro caractere

#list: é uma coleção de dadoos, é bastante flexivel no sentido dos tipos de dados que uma unica lista pode conter
lista = [1,2,3,4]
#podemos acessar os elementos de uma lista usando identação
print(lista[0])


#tuplas
#uma coleção de dados em sequecia que são imutaveis, uma tupla normalmente é criada colocando uma sequencia de valores entre parenteses separado por virgulas 
# podemos usar a função tuple para criar uma tupla

tupla1 = tuple("ola")
print(tupla1)
lista1 = [2]*3

tupla2 = tuple(lista1)
print(tupla2) #cria uma tupla apartir de uma listas
print(tupla2[0]) #podemos acessar um elemento específico de uma tupla utilizando identação

"""4ºset: em python é uma coleção não ordenada de dados mutaveis que não se repetem
um set pode ser criado com a função set()
elementos em um ser não precisam ser os mesmos
"""
set1 = set([1,2,3,4]) #transformando uma lista em um set
set2 = set("ola")# transformando uma string em um ser
print(set2)
print(set1) 
#não podemos acessar os elementos de um set utilizando indices
#existe varias funções nativas da linguagem python para manipular sets


