"""Entrada e saida de dados: input/print
entrada de dados pode ser feita com a função input()
  - input(): sempre produz um dado do tipo string
saida de dados pode ser feita com a função : imprime na saida de dados padrão
"""

#função print
#sintaxe: print(valor(s), sep= ‘ ‘, end = ‘ ’, file=file, flush=flush)
'''
imprime e pula de linha

para alterar os caracteres de fim de string 
'''
nome = "joao"
idade = 20

print("ola", "meu nome é", nome, "e tenho", idade, "anos", end = "\n") #podemos passar dados de qualquer tipo para a função então esses dados são transformados em string e concatenados

print("o que deve ser impresso no final: ", end = "um exemplo\n") #a palavra chave end dita o que sera impresso no final da execução da  função print 

#f_strng

oi = "nada"
print(f"\noi {oi}")

#str.format() method
b, a = 10, 100

print("o valor de b é {} e o valor de a é {}".format(a,b))

#formatador: 
print(f"preça{2.555: .2f}")

print(f"nome{28: b}")

dado = 2
print(f"{dado: >10}") #o quando a variavel dado sera dislocada para a direita
print(f"{dado: ^20}")

#formatadore de inteiro
"""
d
x
o
b
"""

#imprimir sem a quebra de linha
"""
.join() method
(*) operator
"""
#.join(): podemos utilizar para combinar elementos de um objeto interavel em uma unica string
words = ["hellow", "word"]
print("".join(words))
#*: usando um asterisco podemos desempacotar uma string ou tupla e imprimir na tela sem adicionar uma nva linha entre eles  
l = [1,2,3,4,5]
print(*l)


#inputS
"""
input(): a função input retorna uma string
para atribuir um valor a uma variavel com entrada de dados usando input temos que usar typecast
split()
map()
list comprehension
"""
exemplo = input("ascrecente algo para ser impresso na tela")


print(f"o conteudo dado de exemplo para mostrar a função print foi:{exemplo}")

print("imprimindo o conteudo utilizando a função format: {}".format(exemplo))

try: 

    altura: float | int = float(input("digite a altura: ")) #Caso você queira transformar o valor de entrada
    print(f"a altura digitada é: {altura}")

    print(type(altura)) 
except:
    print("altura não é valida")

#multiplos imputs usando o split

x, y = input("digite dois valores: ").split()

print(f"numero de x: {x}")
print(f"numero de y: {y}")

#map() utilizando a função map podenos converter
a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
print("Sum:", a + b + c)


#umltiplos inputs utilizando List comprehension
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)