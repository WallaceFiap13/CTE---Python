Listaaa = [1,7,8,25,9,15]

maximo = Listaaa[0]
minimo = Listaaa[0]

for e in Listaaa:
    if e > maximo:
        maximo = e     
    if e < minimo:
        minimo = e
print(maximo)
print(minimo)

