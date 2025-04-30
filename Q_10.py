notas = list(map(float, input("Digite as notas separadas por espaço: ").split()))

media = sum(notas) / len(notas)

print(f"A sua média é: {media:.2f}")