'''
Importante informar que vários elementos são informados com um colchete; No anterior, como era um só, foi a chave.
'''
comprinhas = [
    {"descrição": "Arroz", "preço": 30.00},
    {"descrição": "Feijão", "preço": 12.50},
    {"descrição": "Macarrão", "preço": 7.00},
    {"descrição": "Carne", "preço": 40.00},
    {"descrição": "Café", "preço": 10.50}
]

for produto in comprinhas:
    print(f"Descrição: {produto['descrição']}, Preço: {produto['preço']}")