#Array list de países
paises = []

'''
O loop for é iniciado pela variável i que receberá valores de 0 a 4 que, neste caso, serão os 5 países solicitados.
'''
for i in range(5):
    pais = input("Por favor, informe o nome de um país: ")
    '''
    O array paises terá novos incrementos toda vez que o usuário digitar um novo pais. 
    '''
    paises.append(pais)
#Mais uma vez usei join pra ficar minimamente aceitável
print(', '.join(paises))