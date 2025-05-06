preco = 1000
desconto = 15

valor_final = preco - (preco * desconto / 100)
print(
	f"\n O preço do celular de Maria com {desconto}% de desconto "
	f"é de R$ {valor_final:,.2f}"
)
