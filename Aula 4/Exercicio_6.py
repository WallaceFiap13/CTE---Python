n = int(input("\nTabuada do: "))
x = 1 # Contador

print(f"\n{x}x{n} = {x*n}")

while x < 10:
    x += 1
    print(f"{x}x{n} = {x*n}")