#uma estrutura de dados que representa uma sequencia de caracteres em python, strings são imutaveis
"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

# criando uma string
String1 = 'ola'
print(String1)


String1 = "ola"
print(String1)

String1 = '''ola"'''
print(String1)

String1 = '''uma string
            com três
            linhas'''
print("\ncriando uma string multipla: ")
print(String1)

#podemos acessar os characteres ispecíficos com o indice

print("primeiro indice", String1[0])
print("ultimo índice", String1[-1])# podemos acessar os elementos   de trás pra frente cutilizando índices ngativos 

#fatiamento de string
#fatiamento[inicio: fim: paço]
string2 = String1[0:3]
print(string2) #o primeiro argumento é o inicio e o ultimo é o fim


#alterando um caractere de uma string podemos alterar um caractere de uma string em python

string1 = "ola mundo"

lista1 = list(string1)
lista1[1] = 'p'
string2 = ''.join(lista1)
string3 = string1[0] + 'p' + string1[2:]

print(string2)
print(string3)


#string format
# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)

# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('exemplo',
                                          'de', 
                                          'teste')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks",
                                                    2009)
print(String1)

#concatenação de string
concatenacao = "junção " + "de " +"strings " +"com " +"o " +"operador "+"de "+"soma"
print(concatenacao)

#f-string(formatação de string)
nome = "luiz"
idade = "20"
fstring = f"o nome escrito foi {nome}, e a idade desse sujeito é {idade}"
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')


#interpolação String
nome = "queijo"
preco = 20
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)


"""
Em Python, caracteres de escape são usados para representar caracteres que não podem ser inseridos diretamente em uma string. Eles começam com uma barra invertida (\). Aqui estão alguns dos principais caracteres de escape:

\\ - Barra invertida
\' - Apóstrofo
\" - Aspas
\n - Nova linha
\t - Tabulação
\r - Retorno de carro
\b - Retrocesso
\f - Alimentação de formulário
\v - Tabulação vertical
\0 - Nulo (caractere de valor 0)
"""

"""Metodos específicos para manipulação de string em python


"""

