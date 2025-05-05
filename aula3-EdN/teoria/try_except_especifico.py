"""
Preciso instanciar um numerador, um denominador e o resultado dessa divisão

Erros:

Se não for valor escreva (Inserir apenas numeros)

Se o denominador for 0 escreva (Não é possível dividir por zero)

"""
try:
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    resultado = numerador / denominador
    print(f"o Resultado é {resultado}")
except ValueError:
    print("Insira apenas números")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
