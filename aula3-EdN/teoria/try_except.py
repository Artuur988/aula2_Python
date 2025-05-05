# Trata erro de conversão de tipo
try:
    # Codigo que pode gerar um erro
    numero = int(input("Digite um número: "))
except ValueError:
    # Codigo executado se ocorrer um erro
    print("Você digitou um número inteiro! Por favor, verifique.")
