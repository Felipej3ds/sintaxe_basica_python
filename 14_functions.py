"""
1. Funções 
2.keywords and positional Arguments
3. Escopo logal e global de variaveis
4. o uso do pass em funções
5.  python range
6. *args() e *kwargs()
7. closure
8. argumento nomeado e não nomeado
9. função map
10. função filter
11. função Reduce
12. função lambda
"""

#1. Função

def funcao(parametro: int, parametro2: float) -> int:
    # Podemos criar uma função em Python com a palavra-chave 'def'.
    # O número passado dentro dos parênteses são os argumentos.
    valor = parametro -  parametro2
    # A função retorna o primeiro parâmetro convertido para um inteiro (não necessário, já é int).
    return valor


#2.keyword and Positional argument: uma maneira de passar um argumento durante a chamada de uma função
"""
keyword only argument : o nome do parametro é usado para passar o valor como argumento durante a chamada da função
positional only argument: passamos os argumentos pela ordem que os paramentros foram definidas na função
""" 
a, b = 2, 2.2
keyword = funcao(parametro2=b, parametro=a)
positional = funcao(b,a)
print(f'keyword argument: {keyword}\npositional argument: {positional}')


#3. escopo de variaveis( local e global)

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

#4. o uso do pass em python 
"como criar uma função vazia utilizando a declaração pass"
def vazia():
    pass

#5. função range em python
"""
a função range retorna uma sequencia de numeros em intervalo definido
range(inicio, fim, intervalo)
"""

while True: #um exemplo da utilização da função range para imprimir numero pares

    try:
        contador = 0
        i = int(input("\ndigite um numero inteiro: "))    
        for n in range(0,i,2):
            print('[',n,']' , sep = '')
            contador += 1
        print(contador, " numeros pares")
        break
    except ValueError:
        print("você não digitou um numero inteiro:")


#6. *args e *kwargs 
"""
o que * um asterisco e um **asteriscoduplo fazem para paremetros em python
a sintaxe *args é usada para passar um numero variado de argumentos para ua função; a variavel que associamos com * se torna um iteravel 
"""

def args(*args):
    for arg in args:
        print(arg)

def kwargs(**kwargs): #utilizada para passar a lista de argumentos keyworded de tamanho variado, podemos pensar no lwargs como um dicionario
    for i, p in kwargs.items( ):
        print(f"{i}:",f"{p}º") 

args(2,1,4,5)
kwargs(primeiro = 1, segundo = 2, terceiro = 3, quarto = 4)

#7. closures
"""

O fechamento do Python é uma função aninhada que nos permite acessar variáveis ​​da função externa mesmo depois que a função externa é fechada.
nested functions: uma função dentro de outra função
"""
def funcao_Externa():
    variavel = 'a variavel da função externa pode ser acessada mesmo após o fechamento da função'
    def funcao_interna():
        print(variavel)
    return funcao_interna
   

oi = funcao_Externa()

oi()


#10. função map()
"""
syntax: map(fun, iter)
fun:é a funçaõ que o map passa cada elemento do iteravel dado
o retorno da função map pode ser passado para a função list para criar uma lista e set() para criar um set
"""
def adicao(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(adicao, numbers)
print(list(result))


#11. função filter()
"""
filtra uma dada sequencia com a ajuda de um metodo que testa cada elemento com a ajudad e uma função que testa cada elemento da sequencia

Syntax: filter(function, sequence)


"""
def fun(variaveis):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variaveis in letters):
        return True
    else:
        return False


# sequence
sequencia = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtrado = filter(fun, sequencia)

print('Tas letras fultradas foram')
for s in filtrado:
    print(s)