# encoding: utf-8
print('Cálculo de média\n')
nota01 = float(input('Insira a nota do 1º bimestre: '))
nota02 = float(input('Insira a nota do 2º bimestre: '))
nota03 = float(input('Insira a nota do 3º bimestre: '))
nota04 = float(input('Insira a nota do 4º bimestre: '))
notafinal = (nota01 + nota02 + nota03 + nota04) / 4

notafinal = "{:.0f}".format(notafinal)
print(f"A nota final é {notafinal}")