L = [1,7,8,25,9,15]

maximo = L[0]
minimo = L[0]

for e in L:
    if e > maximo:
        maximo = e     
    if e < minimo:
        minimo = e
print(maximo)
print(minimo)

