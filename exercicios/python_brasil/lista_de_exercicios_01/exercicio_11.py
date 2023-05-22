#encoding: utf-8
import os
import time

print("Cálculo de 2 números inteiros e 1 real")
int_a = int(input("Insira o valor inteiro A: "))
int_b = int(input("Insira o valor inteiro B: "))
float_a = int(input("Insira um valor real C: "))

total_a = (int_a * 2) * (int_b / 2)
total_b = (int_a * 3) + float_a
total_c = float_a ** 3
os.system("cls")
os.system("clear")
print(f"Produto do dobro do valor A com metade do valor B: {total_a}")
time.sleep(5)

os.system("cls")
os.system("clear")
print(f"Soma do triplo do valor A com o valor C: {total_b:.1f}")
time.sleep(5)

os.system("cls")
os.system("clear")
print(f"Valor C elevado ao cubo: {total_c:.1f}")
time.sleep(5)
os.system("cls")
os.system("clear")