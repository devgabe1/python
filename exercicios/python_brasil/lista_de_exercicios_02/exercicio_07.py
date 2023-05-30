#encoding: utf-8
print("Mostrar maior e menor valor")
maior = float("-inf")
menor = float("inf")

num1 = float(input("Insira um valor: "))
num2 = float(input("Insira um valor: "))
num3 = float(input("Insira um valor: "))

numeros = [num1, num2, num3]

for num in numeros:
    if num < menor:
        menor = num
    elif num > maior:
        maior = num

print(f"O maior valor é {maior:.2f}")
print(f"O menor valor é {menor:.2f}")