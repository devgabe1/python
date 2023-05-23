#encoding: utf-8
print("Cálculo de multa por excesso de pesca\n")

peso = float(input('Insira a quantidade de peixes em Kg: '))

if (peso > 50):
    excesso = (peso - 50)
    multa = (excesso * 4)
    print(f"Excesso: {excesso:.2f}kg")
    print(f"A multa será de R$: {multa:.2f}")

else:
    print("Quantidade dentro dos padrões, não haverá taxas.")
