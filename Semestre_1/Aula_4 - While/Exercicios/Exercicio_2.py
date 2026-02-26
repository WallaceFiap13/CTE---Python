n = int(input("\nTabuada do: "))
inicio = int(input("\nIniciar tabuada no: "))
fim = int(input("\nTerminar tabuada no: "))

print(f"\n{inicio}x{n} = {inicio*n}")

while inicio < fim:
    inicio += 1
    print(f"{inicio}x{n} = {inicio*n}")