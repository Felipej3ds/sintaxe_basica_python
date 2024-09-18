"""
1. Funções 
2. Escopo logal e global de variaveis
3. o uso do pass em funções
4.  python range
*args() e *kwargs()
closure
Self as Default Argument
Secorators in python
função map
gunção Reduce
função lambda
"""

#1. Função

def funcao(parametro: int)-> int: #podemos criar uma funão em python com a palavra chave def, o numero passado dentro do parenteses é o argumento
    #declaração
    return int(parametro)

#2. escopo de variaveis( local e global)

def variavel_local():
    a = 20 
    """
    uma variavel local só é acessivel dentro do escopo dafunção
    """
    return f"a variavel com o valor {a} é local, ou seja as variáveis locais que foram definidas dentro dessa função são desreferenciadas" 
print(variavel_local())
b = 30
def variavel_global():
    global b
    return f"a variavel com valor {b} é global"

print(variavel_global())

#3. o uso do pass em python 

def vazia():
    pass 
"para criar uma função nativa em python usamos a declaração pass"