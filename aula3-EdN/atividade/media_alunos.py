# registrar notas dos alunos

notas = []
alunos = 0

while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

    # verfica se o usuário digitou 'fim' para encerrar o loop

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
            alunos += 1
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")

    except ValueError:
        print("Entrada inválida. Por favor, insira um número de 0 a 10 ou 'fim' para encerrar.")


# Calcular e exibir a média

if alunos > 0:
    media = sum(notas) / alunos
    print(f"A média das notas é: {media:.2f}")
    print(f"Total de alunos: {alunos}")
else:
    print("Nenhuma nota válida foi registrada.")
