#encoding: utf-8
import os
import time
from colorama import init, Fore, Back, Style
init()

os.system("cls")

print("Cálculo de descontos")
valor_hr = float(input("Insira o valor da hora trabalhada R$: "))

hr = float(input("\nInsira a quantidade de horas trabalhadas: "))

time.sleep(1)
sal_bruto = valor_hr * hr
valor_ir = sal_bruto * 0.11
valor_inss =  sal_bruto * 0.08
valor_sind = sal_bruto * 0.05
descontos = valor_ir + valor_inss + valor_sind
sal_liquido =  sal_bruto - descontos
os.system("cls")

print(Fore.YELLOW + Style.BRIGHT + f"Salário Bruto: R$: {sal_bruto:.2f}")
print(Fore.RED + Style.BRIGHT + f"IR (11%): R$: {valor_ir:.2f}")
print(f"INSS (8%): R$: {valor_inss:.2f}")
print(f"Sindicato (5%): R$: {valor_sind:.2f}")
print(Fore.GREEN + Style.BRIGHT + f"Salário Liquido: R$: {sal_liquido:.2f}")





