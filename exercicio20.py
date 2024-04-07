# Define a função para encontrar o maior número
def maiorNumero(n1, n2, n3):
    return max(n1, n2, n3)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = maiorNumero(num1, num2, num3)

print(f"O maior número entre {num1}, {num2} e {num3} é {maior}.")