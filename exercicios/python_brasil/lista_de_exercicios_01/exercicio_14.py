#encoding: utf-8
from colorama import init, Fore, Back, Style
import os
init()

print("Cálculo de multa por excesso de pesca\n")

peso = float(input('Insira a quantidade de peixes em Kg: '))

if (peso > 50):
    excesso = (peso - 50)
    multa = (excesso * 4)
    os.system("clear")
    print(Fore.RED + Style.BRIGHT + f"Excesso: {excesso:.2f}kg")
    print(f"A multa será de R$: {multa:.2f}")

else:
    os.system("clear")
    print(Fore.GREEN + Style.BRIGHT + "Quantidade dentro dos padrões, não haverá taxas.")
