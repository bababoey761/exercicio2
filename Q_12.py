valor = float(input("Qual o valor do produto? R$ "))
pagamento = int(input("Qual sera a forma de pagamento? \n 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto \n 2 - À Vista no cartão de crédito, recebe 10% de desconto \n 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros \n 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%\n "))

if pagamento == 1:
    valor = valor - (valor * 0.15)
elif pagamento == 2:
    valor = valor - (valor * 0.10)
elif pagamento == 3:
    valor = valor
elif pagamento == 4:
    valor = valor + (valor * 0.10)
else:
    print("Opção inválida")
    exit()

print(f"O valor a ser pago sera de R$ {valor:.2f}")