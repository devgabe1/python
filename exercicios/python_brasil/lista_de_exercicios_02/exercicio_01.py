#encoding: utf-8
import os
os.system("cls")
os.system("clear")

print("Calculando número maior.")
num1 = float(input("Insira um valor: "))
num2 = float(input("Insira outro valor: "))

if num1 > num2:
    num_maior = num1

elif num2 == num1:
    print("Os valores são iguais.")

else:
    num_maior = num2
    print(f"O valor maior é {num_maior:.1f}")