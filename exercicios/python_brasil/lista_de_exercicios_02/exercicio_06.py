#encoding: utf-8
print("Mostrar maior número")
num_maior = float("-inf")

num1 = float(input("Insira um valor: "))
num2 = float(input("Insira um valor: "))
num3 = float(input("Insira um valor: "))

numeros = [num1, num2, num3]

for afansfoasofi in numeros:
    if afansfoasofi > num_maior:
        num_maior = afansfoasofi

print(f"{num_maior:.0f}")
