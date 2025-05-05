"""
Uma calculadora

"""

while True:
    try:
        # Numeros com interação do usuario
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida. Use +, -, * ou /.")

        print(f"Resultado: {resultado}")
        break

    except ValueError as e:
        if str(e) == "Operação inválida.":
            print(e)
        else:
            print("Insira apenas números válidos, por favor digite novamente.")

    except ZeroDivisionError as e:
        print(e)
