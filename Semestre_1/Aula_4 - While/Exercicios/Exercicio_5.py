x = 1
y = 0 # Somador
z = 0 # Contador

print("\n")

while x != 0:
    x = int(input("Insira um número inteiro = "))
    y += x
    z += 1

print(f"\nQuantidade de números digitados = {z-1}")
print(f"\nSoma dos números digitados = {y}")
print(f"\nMédia aritimética dos números digitados = {y/(z-1):.2f}\n")
