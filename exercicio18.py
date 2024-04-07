# Define o maior, que chamarei de máximo
def maximo(n1, n2, n3, n4):
    return max(n1, n2, n3, n4)

# Define o dobro
def dobro(n):
    return 2 * n

'''
Aqui os números são convertidos pra Float, caso o usuário faça isso no primeiro momento...
'''
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

maior = maximo(num1, num2, num3, num4)
dobrado = dobro(maior)

print(f"O maior número é {maior} e o dobro dele é {dobrado}.")