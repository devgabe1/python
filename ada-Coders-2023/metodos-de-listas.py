lista = [1, 3, 12, 8, 2]

# append
print('Antes do append:', lista)
lista.append(3)
print('Depois do append:', lista)

# insert
lista.insert(2, 10)
print('Depois do insert:', lista)

# extend
lista2 = [1, 2, 3]
lista.extend(lista2)
print('Depois do extend:', lista)

# pop

lista.pop()
print('Depois do pop:', lista)
lista.pop(0)
print('Depois do pop com parametro:', lista)

# remove
lista.remove(3)
print('Depois do remove:', lista)

# count
print('Quantidade de 2 na lista:', lista.count(2))

# index

print('Índice do elemento 12:', lista.index(12))

# sort
lista.sort(reverse=True)
print(lista)

# FUNÇÕES
# len
print(len(lista))

# sum
print(sum(lista))

# max
print('Maior elemento da lista:', )