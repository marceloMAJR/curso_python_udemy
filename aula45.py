"""
Iterável -> str, range, etc (__iter__)
Iterável -> quem sabe entregar um valor por vez
next -> me entrega o próximo valor
iter -> me entrega seu iterador
"""
# for letra in texto
texto = iter('Marcelo') # iterável

# iteratador = iter(texto) # iterador

# while True:
#     try:
#         print(next(iteratador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)