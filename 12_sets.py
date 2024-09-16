#uma coleção de dados distintos e não ordenados um set é uma estrutuda de dados mutavel

"""

"""

# Criando sets
set1 = {1, 2, 3, 4}
set2 = set([2, 3, 4, 5])
set3 = set()  # Set vazio

# Adicionando elementos
set3.add(6)
set3.add(7)

# Removendo elementos
set1.discard(1)  # Remove o elemento 1 se existir, sem lançar erro se não existir
set2.remove(5)   # Remove o elemento 5, lançará erro se o elemento não existir

# Verificando a presença de elementos
print(4 in set1)  # Saída: False, porque 4 foi removido de set1
print(6 in set3)  # Saída: True, porque 6 foi adicionado a set3

# Operações matemáticas com sets
uniao = set1 | set2  # União dos dois sets
interseccao = set1 & set2  # Interseção dos dois sets
diferenca = set1 - set2  # Diferença entre set1 e set2
diferenca_simetrica = set1 ^ set2  # Diferença simétrica entre set1 e set2

# Exibindo resultados
print("Set1:", set1)  # Saída: Set1: {2, 3, 4}
print("Set2:", set2)  # Saída: Set2: {2, 3, 4}
print("Set3:", set3)  # Saída: Set3: {6, 7}
print("União:", uniao)  # Saída: União: {2, 3, 4}
print("Interseção:", interseccao)  # Saída: Interseção: {2, 3, 4}
print("Diferença:", diferenca)  # Saída: Diferença: set()
print("Diferença Simétrica:", diferenca_simetrica)  # Saída: Diferença Simétrica: set()