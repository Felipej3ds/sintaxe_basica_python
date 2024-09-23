# Tipos de Dados em Python

# Os tipos de dados são conceitos importantes em qualquer linguagem de programação para armazenamento e manipulação de dados.
# Em Python, os principais tipos de dados são:
"""
1. Tipos Numéricos: {int, float, complex}
2. Tipos Sequenciais: {list, tuple, range, str}
3. Tipo Dicionário: dict
4. Tipo Conjunto: {set, frozenset}
5. Tipo Booleano: bool
6. Tipos Binários: {bytes, bytearray, memoryview}
"""
string = [1,2,3]

# Os tipos de dados determinam quais operações podem ser realizadas com uma variável.
# Em Python, os tipos de dados são classes e as variáveis são instâncias dessas classes.
# As classes que representam os tipos de dados possuem métodos para manipulação.

# Observação: Podemos saber o tipo de dado de qualquer variável utilizando a função type().

# 1. Tipos Numéricos
# São dados que possuem valores numéricos, podendo ser:
# Inteiros (int), Flutuantes (float) e Complexos (complex)

inteiro = 2  # Números inteiros
flutuante = 2.2  # Números de ponto flutuante
complexo = 3 + 2j  # Números complexos

print(f"Inteiro: {inteiro}, Tipo: {type(inteiro)}")
print(f"Flutuante: {flutuante}, Tipo: {type(flutuante)}")
print(f"Complexo: {complexo}, Tipo: {type(complexo)}")

# 2. Tipos Sequenciais
# Permitem armazenar dados de maneira ordenada.

# Strings
string1 = "meu nome"  # Uma sequência de caracteres Unicode
string2 = """oi
meu nome é
juao
"""
print(f"String: {string2.strip()}")  # Remover espaços em branco
print(f"Primeiro caractere: {string2[0]}")  # Acessando o primeiro caractere

# Listas
lista = [1, 2, 3, 4]  # Coleção de dados flexível
print(f"Lista: {lista}, Primeiro elemento: {lista[0]}")  # Acessando o primeiro elemento

# Tuplas
tupla1 = tuple("ola")  # Criando uma tupla a partir de uma string
print(f"Tupla: {tupla1}")

lista1 = [2] * 3  # Lista com repetição de elementos
tupla2 = tuple(lista1)  # Criando uma tupla a partir de uma lista
print(f"Tupla criada a partir da lista: {tupla2}, Primeiro elemento: {tupla2[0]}")

# 4. Sets
# Em Python, um set é uma coleção não ordenada de dados mutáveis que não se repetem.

set1 = set([1, 2, 3, 4])  # Transformando uma lista em um set
set2 = set("ola")  # Transformando uma string em um set
print(f"Set a partir da lista: {set1}")
print(f"Set a partir da string: {set2}")

# Não podemos acessar elementos de um set utilizando índices
# Exemplo de manipulação de sets
set1.add(5)  # Adicionando um elemento
print(f"Set após adicionar 5: {set1}")