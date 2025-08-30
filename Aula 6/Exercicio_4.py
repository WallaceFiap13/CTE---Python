V = [9,8,7,12,0,13,21]
P = []
I = []

for x in V:
    if x %2 == 0:
        P.append(x)
    else:
        I.append(x)

print(f"Pares: {P}")
print(f"Ímpares: {I}")