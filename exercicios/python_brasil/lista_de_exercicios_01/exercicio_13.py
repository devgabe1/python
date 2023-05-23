#encoding: utf-8
print("Cálculo de peso")
altura = float(input("Insira sua altura: "))

peso_h = (72.7 * altura) - 58
peso_m = (62.1 * altura) - 44

print(f"\nHomem - Seu peso ideal é {peso_h:.2f}Kg")
print(f"Mulher - Seu peso ideal é {peso_m:.2f}Kg")