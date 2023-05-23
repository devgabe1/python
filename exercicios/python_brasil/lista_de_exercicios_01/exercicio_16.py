#encoding: utf-8
import math
import os

print("Cálculo de latas de tinta")
tam = float(input("Insina o tamanho em metros quadrados da área a ser pintada: "))
litro_tinta = tam / 3

quant_latas = litro_tinta / 18
quant_latas_arrendodado = math.ceil(quant_latas)

valor_total = quant_latas_arrendodado * 18
os.system("cls")

print(f"Quantidade de latas de tinta necessárias: {quant_latas_arrendodado}")
print(f"Valor gasto: R$: {valor_total:.2f}")