# calculadora.py
# Criado por Ewertom de Souza Silva para o desafio DIO Open Source

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

print("Calculadora Simples")
print("Selecione a operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

escolha = input("Digite a opção (1/2/3/4): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print("Resultado:", somar(num1, num2))
elif escolha == '2':
    print("Resultado:", subtrair(num1, num2))
elif escolha == '3':
    print("Resultado:", multiplicar(num1, num2))
elif escolha == '4':
    print("Resultado:", dividir(num1, num2))
else:
    print("Opção inválida")
