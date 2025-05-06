# Quero saber se a pessoa é idosa, adulta, adolescente, criança ou bebê
idade = int(input("Qual a sua idade? "))

if idade >= 60:
    print("Você é idosa!")
elif idade >= 18:
    print("Você é adulta!")
elif idade >= 12:
    print("Você é adolescente!")
elif idade >= 5:
    print("Você é criança!")
else:
    print("Você é bebê!")
