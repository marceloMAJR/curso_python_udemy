# dir, hasattr e getattr em Python
# string = ' Luiz '
# metodo = 'strip'

# if hasattr(string, metodo):
#     print('Existe upper')
#     print(getattr(string, metodo)())
# else:
#     print('Não existe o método', metodo)

"""
string = '  Luiz  '
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe o método:', metodo)
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
"""

texto = input('Digite uma palavra: ')
print(f'Palavra digitada: {texto}')
metodo = input('Digite um método (upper/lower): ')

if hasattr(texto, metodo):
    print(getattr(texto, metodo)())