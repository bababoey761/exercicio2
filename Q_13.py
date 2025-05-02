nome = input("Digite seu nome: ")
idade =int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida")
    exit()

if idade < 18:
    status = "menor de idade"
else:
    status = "maior de idade"

print(f"Olá {nome}, você tem {idade} anos e é {status}.")