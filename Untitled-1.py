Cons = int(input("Digite o consumo: "))
Tipo = input("Digite o tipo de instalação (R, I ou C): ")

if Cons < 1000 and Tipo == "R":
    valor = Cons * 0.65
    print(f"Valor a pagar: R${valor:.2f}")
elif Cons < 1000 and Tipo == "C":
    valor = Cons * 0.70
    print(f"Valor a pagar: R${valor:.2f}")
elif Cons < 5000 and Tipo == "I":
    valor = Cons * 0.60
    print(f"Valor a pagar: R${valor:.2f}")
else:
    print("Inválido.")