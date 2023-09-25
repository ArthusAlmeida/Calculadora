# Função para somar dois números
def adicao(x, y):
    return x + y

# Função para subtrair dois números
def subtracao(x, y):
    return x - y

# Função para multiplicar dois números
def multiplicacao(x, y):
    return x * y

# Função para dividir dois números
def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    else:
        return x / y

# Menu de opções
print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Solicitar ao usuário que escolha uma opção
escolha = input("Digite a opção (1/2/3/4): ")

# Solicitar ao usuário que insira dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Executar a operação com base na escolha do usuário
if escolha == '1':
    print("Resultado:", adicao(num1, num2))
elif escolha == '2':
    print("Resultado:", subtracao(num1, num2))
elif escolha == '3':
    print("Resultado:", multiplicacao(num1, num2))
elif escolha == '4':
    print("Resultado:", divisao(num1, num2))
else:
    print("Opção inválida")
