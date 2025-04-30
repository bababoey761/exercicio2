valor1 = int(input("Digite o primeiro valor: "))
valor2= int(input("Digite o segundo valor: "))

bool1 = bool(valor1)
bool2 = bool(valor2)

if bool1 and bool2:
    print("Ambos os valores são verdadeiros")
elif not bool1 and not bool2:
    print("Ambos os valores são falsos")
else:
    print("Um valor é verdadeiro e o outro é falso")