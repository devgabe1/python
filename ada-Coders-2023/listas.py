lista = [10, 'Gabriel', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

print(lista[0:3])
print(lista[0:])
print(lista[0:4:2])

for c in lista:
    print(c)

print('Comprimento da lista:', len(lista))

for c in range(len(lista)):
    print(c)