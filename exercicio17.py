# Um Define para cada operação básica
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

'''
No caso da multiplicação e divisão, que pode gerar dízimas periódicas, utilizei a função Round que é muito similar ao format do Java. Porém, muito + fácil de ser aplicada! :D
'''
def multiplicacao(a, b):
    return round(a * b, 2)

def divisao(a, b):
    if b != 0:
        return round(a / b, 2)
    else:
        return "Erro: nada de divisão por zero mané!"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# "Chama" os cálculos graças ao Define
print(f"Soma de {num1} e {num2} é {adicao(num1, num2)}.")
print(f"Subtração de {num1} por {num2} é {subtracao(num1, num2)}.")
print(f"Multiplicação de {num1} e {num2} é {multiplicacao(num1, num2)}.")
print(f"Divisão de {num1} por {num2} é {divisao(num1, num2)}.")