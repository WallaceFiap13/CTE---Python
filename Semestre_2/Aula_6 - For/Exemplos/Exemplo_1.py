L = ["a", "b", "c", "d", "e"]

letra = input("\nDigite a letra a ser procurado:\n")

posicao = 1
indice = 0

for x in L:
    if x == letra: #Se o que está rodando na lista for igual o que a pessoa inputou
        print("\nLetra encontrada!")
        print(f"No índice {indice}")
        print(f"Na posição {posicao}")
        break
    posicao += 1
    indice += 1
else:
    print("\nLetra não encontrada")
