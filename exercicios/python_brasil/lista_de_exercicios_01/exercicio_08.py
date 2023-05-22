#encoding: utf-8
print("Calcular salário")
valor_hr = float(input("Insira o valor da hora trabalhada: "))
hora_mes = float(input("Insira a quantidade de dias trabalhados no mês: "))
valor_total = valor_hr * hora_mes
print(f"O salário será igual a R$: {valor_total:.2f}")