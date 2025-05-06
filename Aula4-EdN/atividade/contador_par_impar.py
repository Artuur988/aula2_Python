# Conta pares e impares 

pares = 0
impares = 0


while True:
    entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")

    # Verifica se o usuário deseja sair
    if entrada.lower() == 'sair':
        print("Encerrando o programa.")
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
            print(f"Número {numero} é par.")
        else:
            impares += 1
            print(f"Número {numero} é ímpar.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
