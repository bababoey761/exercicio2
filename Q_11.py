notas = list(map(float, input("Digite as notas separadas por espaço: ").split()))
if all(nota < 0 or nota > 10 for nota in notas):
    print("Você deve digitar notas entre 0 e 10.")
    exit()
media = sum(notas) / len(notas)
if media >= 7:
    status = "APROVADO"
else:
    status = "REPROVADO"

print (f"média: {media:.2f}\nStatus: {status}")
      