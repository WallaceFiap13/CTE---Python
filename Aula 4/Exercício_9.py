vi = float(input("\nQual seu depósito inicial, em reais?\n"))
am = float(input("\nQual seu aporte mensal, em reais?\n"))
juros = (float(input("\nInsira os juros de rendimento da poupança, em porcentagem\n")))/100

x = 1 # contador 1
y = (vi+(vi*juros) + am+(am*juros)) # acumulador

print("\nEvolução mês a mês:\n")
print("Mês | Saldo acumulado")
print("----------------------")

print(f"\n{x}° Mês = R${y:.2f}")

while x < 24:
    x += 1
    y += am
    y = (y + (y*juros))
    print(f"{x}° Mês = R${y:.2f}")

print(f"\nForam obtidos R${y-vi-(24*am):.2f} de ganho com juros\n")