#estruturas de repetição para manipulação de dados e contrução de códigos mais concisos

"""
for loop
while loop
loop control statement
python compreensão de listas 
python compreensão de dicionarios
"""

#for loop: em python o loop for serve pra iterar sobre objetos iteraveis{listas, tuplas , dicionarios}

"""
for var in intaravel:
    #codigo
"""
#iterar sobe uma string
s = "sim"
j = 1
for i in s:    
    print(i, f"{j}º iteração",)
    if j == 3:
        j = 0
    j += 1


#for loop com o range
for i in range(0, 10, 2):
    print(i, f"{j}º iteração")
    if j == 5:
        j = 0
    j += 1

#for loop com enumerate
print("\n", "enumerate")
lista = {"oi", "sabão", "sapo"}
for contador, i in enumerate(lista):
    print(contador, i, f"{j}º iteração")
    j+=1

#preenhendo uma lista com um loop em uma linha

lista2 = [x for x in range(12)]
print(lista2)


#for loop com um dicionario

d = dict()

d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))

#python for loop with tuple
t = ((1, 2), (3, 4), (5, 6))
for a, b in t:
    print(a, b)

#for loop com a função zip

lista3 = ["voce", "é", "feio"]
lista4 = ["não", "tão", "assim"]
for fruit, color in zip(lista3, lista4):
    print(fruit, color, end = " ")

#Declarações de Controle que podem ser usadas com o Loop for em Python

a = "papaamericano"

for i in a:
    if i == "a":
        continue #o continue retorna o loop pro inicio
    print(i)

for i in a:
    print(i)
else: #o else no for só é executado quando o loop não é interrompido com o break
    print("sem break")



#while
"""
- while loop: repete um bloco de comandos até que uma condição sejá falça
- declarações de controle: 
    continue: retorna o loop para o ínicio
    Break: sai do loop
    pass: utilizado para escrever loops vazios

- sentinel controlled Statement: aqui o usuario decide quantas vezes eçle qque que o loop seja execultado utilizando a sentinel value
"""
i = 2
while (i > 0): #condição
    print(f"{i} não é menor que zero")
    i -= 1 #cuidado com loops infinitos


#sentinel controlled statement
a = 0
while a != -1:
    try:
        a = int(input("acrescente o valor -1: "))
        if a != -1:
            print("você não digitou -1 tente novamente")
    except:
        print("o valor que você digitou não é um numero tente novamente")
        continue

#loop com um valor booleano

contador = 0

while True:
    print(f"contador = {contador}")
    contador += 1
    if contador == 10:
        print(f"contador = {contador}")
        break

#while com else

i = 5
while i > 0:
    print("condição satisfeita")
    i -= 1
else:  #o else não sera executado caso o loop termine com um break ou com uma excessão
    print("condição não mais satisfeita", print("\nloop terminado sem break"))



#Dictionary Comprehension
keys = ["a", "b", "c"]
valores = [1,2,3]

dicionario ={ k:v for (k,v) in zip(keys, valores)}

print(dicionario)


#fromkey()
dic=dict.fromkeys(range(5), True)

print(dic)