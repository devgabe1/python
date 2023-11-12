def saudacao():
    print('Seja bem vindo!')
    print('Olá, é um prazer ter você fazendo parte desse curso')

def saudacao2(nome, curso):
    print(f'Seja bem vindo, {nome}')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

def saudacao3(nome, curso = 'Python'):
    print(f'Seja bem vindo, {nome}')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

def soma(num1, num2):
    return num1 + num2

resultado = soma(4, 5)
print(resultado)
