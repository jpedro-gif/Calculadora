def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero"
    return a / b


print("=== CALCULADORA ===")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("\nEscolha uma operação (1-4): ")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if opcao == "1":
    print(f"\nResultado: {somar(a, b)}")
elif opcao == "2":
    print(f"\nResultado: {subtrair(a, b)}")
elif opcao == "3":
    print(f"\nResultado: {multiplicar(a, b)}")
elif opcao == "4":
    print(f"\nResultado: {dividir(a, b)}")
else:
    print("\nOpção inválida!")