from datetime import date

ano_nascimento = int(input("Digite o ano em que você nasceu: "))
mes_nascimento = int(input("Digite o mês em que você nasceu (1-12): "))
dia_nascimento = int(input("Digite o dia em que você nasceu (1-30): "))

data_atual = date.today()

data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)

diferença = data_atual - data_nascimento

idade_anos = diferença.days // 365
idade_meses = (diferença.days % 365) // 30
idade_dias = (diferença.days % 365) % 30

print(f"Você já viveu aproximadamente:")
print(f"{idade_anos} anos, {idade_meses} meses e {idade_dias} dias.")