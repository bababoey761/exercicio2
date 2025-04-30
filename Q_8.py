valores = list(map(int, input("Digite 3 valores divididos por espaço: ").split()))
if len(valores) != 3:
    print("Você deve digitar exatamente 3 valores.")
    exit()

valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são:{valores}")