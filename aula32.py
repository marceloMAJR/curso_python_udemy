"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Exercício 1
try:
    num_int = int(input('Digite um número inteiro: '))
    if num_int % 2 == 0:
        print(f'{num_int} é par.')
    elif num_int % 2 != 0:
        print(f'{num_int} é ímpar.')
except:
    print('Valor digitado não é um número inteiro.')

# Exercício 2
try:
    hora = int(input('Digite alguma hora: '))
    if hora > 23:
        print('Você digitou uma hora inexistente.')
    elif hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora > 11 and hora <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    print('Valor digitado não é um número inteiro.')

# Exercício 3
primeiro_nome = input('Digite seu primeiro nome: ')
len_nome = len(primeiro_nome)

if len_nome <= 1:
    print('Digite mais de uma letra.')
elif len_nome <= 4:
    print('Seu nome é curto.')
elif len_nome > 4 and len_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande.')
