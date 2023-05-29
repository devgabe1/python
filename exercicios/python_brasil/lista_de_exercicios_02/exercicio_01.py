#encoding: utf-8
import os
os.system ("cls")
os.system ("clear")

print("Calculando número maior.")
num1 = int(input("Insira um valor: "))
num2 = int(input("Insira outro valor: "))

if num1 > num2:
    num_maior = num1
else:
    num_maior = num2

print(f"O valor maior é {num_maior:.0f}")