A = int(input("Fale o valor de A: "))
B = int(input("Fale o valor de B: "))
C = int(input("Fale o valor de C: "))

soma = A + B

if soma < C:
    print (f"O valor da soma é {soma} sendo menor que C({C})")

elif soma == C:
    print (f"O valor da soma é {soma} sendo igual a C({C})")

else:
    print (f"O valor da soma é {soma} sendo maior que C({C})")