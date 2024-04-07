compras = [
    {"descrição": "Arroz", "preço": 30.00},
    {"descrição": "Feijão", "preço": 12.50},
    {"descrição": "Macarrão", "preço": 7.50},
    {"descrição": "Carne", "preço": 40.00},
    {"descrição": "Café", "preço": 10.50}
]

maisCaro = compras[0]
maisBarato = compras[0]

'''
O For, basicamente, faz uma verificação de cada item e identifica o maior e o menor valor.
'''
for produto in compras:
    if produto["preço"] > maisCaro["preço"]:
        maisCaro = produto
    if produto["preço"] < maisBarato["preço"]:
        maisBarato = produto

print(f"Produto mais caro: {maisCaro
['descrição']}, Preço: {maisCaro['preço']}")
print(f"Produto mais barato: {maisBarato
['descrição']}, Preço: {maisBarato['preço']}")