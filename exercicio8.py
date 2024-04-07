numerozim = []

# Peça ao usuário 10 números diferentes
for i in range(10):
    '''
    Converte os números informados em inteiros até chegar à repetição número 10. Há um incremento dentro do input, para garantir que isto ocorra.
    '''
    numero = int(input(f"Por favor, digite o número {i+1}: "))
    '''
    Caso o número seja par, ou resto 0, será adicionado o valor 100 a este número par em questão.
    '''
    if numero % 2 == 0:
        numero += 100
    
    numerozim.append(numero)

for i, numero in enumerate(numerozim):
    print(f"Número {i+1}: {numero}")