'''


'''


def gorjeta(valor_conta, porcentagem_gorjeta):
    '''
    Função que calcula o valor da gorjeta e o valor total a ser pago.
    
    Parâmetros:
    valor_conta (float): Valor da conta.
    porcentagem (float): Porcentagem da gorjeta.
    gorjeta (float): Valor da gorjeta. Padrão é 0.
    
    Retorna:
    float: Valor da gorjeta.


    '''
    
    # Calcula o valor da gorjeta
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    
    return round(gorjeta, 2)

total_conta = float(input('Digite o valor da conta: '))
porcentagem = float(input('Digite a porcentagem da gorjeta: '))
    
valor_gorjeta = gorjeta(total_conta, porcentagem)
print(f'A sua conta de R$ {total_conta} com gorjeta de {porcentagem}% é R$ {valor_gorjeta}')
	