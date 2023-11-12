dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Gabe', 'idade': 20, 'altura': 1.70}

print(dicionario)
print(dicionario['idade'])

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2
print(dicionario)

for c in dicionario:
    print(c, dicionario[c])

print('peso' in dicionario)
print('altura' in dicionario)