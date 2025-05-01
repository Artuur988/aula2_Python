# Calculadora de IMC
# peso dividido pela altura ao quadrado
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura**2)
print("Seu IMC é de {:.1f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Você está com o peso normal.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
elif imc < 34.9:
    print("Você está com obesidade grau 1.")
elif imc < 39.9:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3.")
