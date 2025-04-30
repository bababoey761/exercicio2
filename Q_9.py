peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / altura ** 2

if peso <= 0 or 3 < altura <= 0:
    print("peso e/ou altura inválidos")
    exit()

if imc <= 18.5:
    status = "Abaixo do peso"
elif 18.5 < imc < 25:
    status = "Peso ideal(Parabéns!)"
elif 25 <= imc < 30:
    status = "Levemente acima do peso"
elif 30 <= imc < 35:
    status = "Obesidade de grau I"
elif 35 <= imc < 40:
    status = "Obesidade de grau II (severa)"
elif imc >= 40:
    status = "Obesidade de grau III (mórbida)"

print(f"Seu IMC (Índice de Massa Corporal) é {imc:.2f} e você se encaixa na categoria {status}.")