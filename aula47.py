"""
Faça um jogo para advinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e
vai dar a possibilidade para o usuário digitar apenas uma letra
- Quando o usuário digitar uma letra, você vai conferir se a letra
digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
nmr_tentativas = 0

while True: # laço para rodar o jogo inteiro
    letra_digitada = input('Digite uma letra: ')
    nmr_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta 
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns! Você descobriu a palavra secreta.')
        print('A palavra secreta era', palavra_secreta)
        print('Tentativas:', nmr_tentativas)
        print('FIM DE JOGO!')

    
