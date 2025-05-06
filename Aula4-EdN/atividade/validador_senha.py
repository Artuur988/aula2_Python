# Verificar se a senha é forte, tendo 8 digitos e ao menos 1 número

while True:
    senha = input("Digite sua senha(ou 'sair' para encerrar): ")


    # Verifica se o usuário deseja sair
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break

    tem_numero = False

    # Verifica se a senha tem numero

    for char in senha:
        if char.isdigit():
            tem_numero = True
            break

    # Precisa ter 8 caracteres e pelo menos 1 número

    if len(senha) <8:
        print("A senha precisa ter pelo menos 8 caracteres.")
    elif not tem_numero:
        print("A senha precisa ter pelo menos 1 número.")
    else:
        print("Senha forte!")
        break
