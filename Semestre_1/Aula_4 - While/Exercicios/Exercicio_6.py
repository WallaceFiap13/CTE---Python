
codigo = 1
x = 0 # Somador

while codigo != 0:
    codigo = int(input("\nDigite o código do produto = "))

    if codigo == 1:
        qtd = int(input("Digite a quantidade comprada do produto = "))
        x += qtd*0.5

    elif codigo == 2:
        qtd = int(input("Digite a quantidade comprada do produto = "))
        x += qtd*1

    elif codigo == 3:
        qtd = int(input("Digite a quantidade comprada do produto = "))
        x += qtd*4

    elif codigo == 5:
        qtd = int(input("Digite a quantidade comprada do produto = "))
        x += qtd*7

    elif codigo == 9:
        qtd = int(input("Digite a quantidade comprada do produto = "))
        x += qtd*8
    
    elif codigo == 0:
        print("Compra finalizada!!")

    else:
        print("Código inválido")

    print("\n------------------------------------------")

print(f"\nO valor total das suas compras é de R${x:.2f}\n")
print("------------------------------------------\n")