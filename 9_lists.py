#uma coleção de dados fechado por [] e separados por virgulas, focaremos mais nos metodos para se trabalhar com listas em python

var = ["lista", "de", "exemplo"]

a, b, c = var

print(a, b, c) #desempacotamento de listas
print(*var)


#podemos acessar os elementos pelos indices ex:
print(var[0])

#tambem podemos alterar os valores utilizando os indices
var[0] = "nova lista"

var.append("2") #adiciona um item no final da lista

var.extend([3,4,5]) #adiciona os elementos de um interavel no final de uma lista

var.insert(0, 1) #adiciona um elemento na posição dada, primeiro argumento é a posição

var.remove(3) #remove um elemento de um valor da lista

print(var.index(4)) #reterna o indice do primeiro elemento que possuir o mesmo valor do argumento 

ultimo_valor = var.pop() #remove o ultimo elemento da lista ou do valor especificado

var.count(5) #retorna a quantidade de vezes que um elemento aparece em uma lista

var.reverse()

del var[2] #deletou o elemento de índice 2 da lista 

var.clear() #remove todos os elementos da lista 


