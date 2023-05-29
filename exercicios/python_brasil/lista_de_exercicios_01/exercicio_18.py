import os
os.system("cls")
print("Calcular tempo médio de download")
tamanho = float(input("Insira o tamanho em Mb do arquivo: "))
veloc = float(input("Insira a velocidade em Mbps do link usado: "))

os.system("cls")
print(f"O tempo aproximado de download do arquivo será de {tamanho / veloc:.2f}s")