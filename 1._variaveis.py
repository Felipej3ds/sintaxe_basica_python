#o que são variaveis

""" são espaços reservados na memoria que podemos Armazenar/Acessa dados 
- variaveis possuem
    - indentificadores(nome)
    - tipos de dados(podem ser convertidos)
    - atribuição(conteudo)
uma variavel é criada no momento que atribuimos um valor a um indentificador(nome)
"""

#Regras de nomeação_de_variaveis:
"""
    o python é uma linguagem case sensitive 
    variaveis não podem ser numeros
    não podem possuir caracteres especiais
    um código não pode ter duas variaveis iguais
    keyword ou palavras chaves não podem ser usada para nomer variaves
"""

"tipos de dados Primitivos"

#int (inteiro)
idade = 20
#str (tipo texto) deve
nome = 'Fulano'
#float (ponto flutuante)
altura = 1.8
#bool: booleano ou lógico (true/false)
fulano_e_menor_de_idade = False

"so sera convertido se for possivel converter"

#python permite atribuir um valor a varias variaveis simultaneamente com o sinal de igual
a = b = c = 20

#python permite atribuir valores a varaiveis diferentes em uma unica linha com a ","
a, b3, c = 20, {'nome': 20, 'idade': 30},False

"""
variaveis podem ser locais ou globais: 
"""
# locais são declearadas dentro de uma função e não conseguimos usar essa variavel fora de função 
def demonstracao():
    variavel_local = "sou local"
    print(variavel_local)

#variaveis globai são acessiveis em qualquer parte do codigo, possuem um escopo global

variavel_global = "eu sou global"
def demonstracao_global():
    #para modificar uma variavel global dentro de uma função devemos usar a palavra chave global
    global variavel_global 
    variavel_global = "eu sou global mas fui modificado dentro da função"
    print(variavel_global)
print(variavel_global)


"""shared Reference
em python variaveis referenciam objetos e podemos criar referencias 
compartilhadas
"""
a = 5 #o python criaou um objeto que representa o valor 5 e referenciou a variavel
y = a #python criou uma variavel y que referencia o mesmo objeto de x
print(a is y)
a = 6 #agora a varaivel a referencia outro objeto enquando o y mantem a referencia ao objeto que representa o valo 5
print(a is y)

"""type notation
utilizado para especificar o tipo esperado para uma variavel
"""
nome2: str = "alguem"
idade2: int = 20
estudante: bool = False

def comprimentar(nome: str) -> str: 
    return f"Hello, {nome}"
#explicita o tipo de dado que a função recebe e o tipo de dado que ela retorna