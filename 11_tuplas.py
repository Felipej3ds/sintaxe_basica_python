#uma estrutura de dados heterogenea, uma sequencia de dados armazenados em sequencia
"""
os valores de uma tupla são sintaticamentes separados por virgulas e colocados entre apresentes()
tuplas são imutaveis 
- criando uma tupla
- acessando tuplas 
- concatenado tuplas    
- deletando tuplas
- tuplas vs listas
"""

#criando tupla
tupla1 = ()
tupla1 = (1,2)
lista = [3,4,5]
tupla2 = tuple(lista)
tupla3 = tuple("exemplo")
tupla4 = (tupla2, tupla3)
tupla5 = (tupla3, ) * 3


#acessando uma tupla
print(tupla1[0])

a, b = tupla4
print(a, b, sep = ('\n'))

#concatenação de tupla (+)
tupla6 = tupla4 + tupla5

"""
funções que podem ser utilizadas tanto para listas como para tuplaslen(), max(), min(), sum(), any(), all(), sorted()
metodos que não podem ser utilizadas para tuplas: append(), insert(), remove(), pop(), clear(), sort(), reverse()

all()
eny()
len()
enumerate()
max()
min()
sum()
sorted()
tuple()
"""