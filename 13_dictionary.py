# Criando um dicionário
dicionario = {
    "Python": "Uma linguagem de programação de alto nível.",
    "List": "Uma estrutura de dados que armazena uma sequência de elementos.",
    "Dict": "Um tipo de dado que armazena pares chave-valor."
}

# Adicionando um novo item
dicionario["Tuple"] = "Uma coleção ordenada e imutável de elementos."

# Atualizando um item existente
dicionario["List"] = "Uma estrutura de dados mutável que armazena uma sequência de elementos."

# Acessando um valor
print(dicionario["Python"])  # Saída: Uma linguagem de programação de alto nível.

# Removendo um item
del dicionario["Tuple"]

# Iterando sobre chaves e valores
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# Verificando se uma chave existe
if "Dict" in dicionario:
    print("A chave 'Dict' está presente no dicionário.")

# Obter todas as chaves e valores
chaves = dicionario.keys()
valores = dicionario.values()

print("Chaves:", list(chaves))
print("Valores:", list(valores))