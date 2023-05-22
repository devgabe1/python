#encoding: utf-8
print("Conversor graus Fahrenheit")
temp = float(input("Insira a temperatura em graus Fahrenheit: "))
temp = 5 * ((temp - 32) / 9)
print(f"A temperatura convertida em Celsius é: {temp:.1f}ºC")