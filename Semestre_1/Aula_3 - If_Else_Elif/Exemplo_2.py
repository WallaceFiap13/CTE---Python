print("\nInsira 3 números e descubra qual é o maior e menor:")

a = int(input("Número a = "))
b = int(input("Número b = "))
c = int(input("Número c = "))

# Maior Número

if a > b and a > c:
    print("\nO número a é o maior")

if b > a and b > c:
    print("\nO número b é o maior")

if c > a and c > b:
    print("\nO número c é o maior")

# Menor Número

if a < b and a < c:
    print("& o número a é o menor")

if b < a and b < c:
    print("& o número b é o menor")

if c < a and c < b:
    print("& o número c é o menor")