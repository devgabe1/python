#encoding: utf-8
print("Apresentar valores em ordem decrescente.")

num1 = float(input("Insira um valor: "))
num2 = float(input("Insira um valor: "))
num3 = float(input("Insira um valor: "))

numeros_lista = [num1, num2, num3]
ordem_crescente = sorted(numeros_lista)

for num in ordem_crescente:
    print(f"{num:.0f}")