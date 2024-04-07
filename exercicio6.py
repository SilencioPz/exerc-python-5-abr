numeros = list(range(1, 11))
'''
Cria uma lista apenas com os números pares, que módulo de 2 gerarão resto 0 e, portanto, serão pares.
'''
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)