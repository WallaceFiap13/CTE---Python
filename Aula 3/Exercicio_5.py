operacao = input("\nInsira a operação que você deseja realizar (Soma, Subtração, Multiplicação ou Divisão)\n")

num_a = int(input("\nInsira o primeiro número = "))
num_b = int(input("Insira o segundo número = "))

if operacao == "Soma":
    print(f"\nO resultado é = {num_a + num_b}")

if operacao == "Subtração":
    print(f"\nO resultado é = {num_a - num_b}")

if operacao == "Multiplicação":
    print(f"\nO resultado é = {num_a * num_b}")

if operacao == "Divisão":
    print(f"\nO resultado é = {num_a / num_b}")