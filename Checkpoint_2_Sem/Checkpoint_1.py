Avaliacao = ["CP1","CP2","CP3", "Sprint1", "Sprint2", "GS"]

CPs1 = []
Sprints1 = []
GS1 = []

CPs2 = []
Sprints2 = []
GS2 = []

Contador = 1
Posicao = 1

while Contador < 3:
    if Contador == 1:
        print("\n1° Semestre")
    
    if Contador == 2:
        print("\n2° Semestre")
        
    for x in Avaliacao:
        Nota = int(input(f"\nInsira a nota do(a) {x} = "))
        
        if Posicao == 1:
            if Avaliacao.index(x) < 3:
                CPs1.append(Nota)
            elif Avaliacao.index(x) < 5:
                Sprints1.append(Nota)
            else:
                GS1.append(Nota)

        elif Posicao == 2:
            if Avaliacao.index(x) < 3:
                CPs2.append(Nota)
            elif Avaliacao.index(x) < 5:
                Sprints2.append(Nota)
            else:
                GS2.append(Nota)

    if Posicao == 1:
        Media_1 = (((sum(CPs1) - min(CPs1)) + sum(Sprints1)) / 4) * 0.4 + GS1[0] * 0.6
    elif Posicao == 2:
        Media_2 = (((sum(CPs2) - min(CPs2)) + sum(Sprints2)) / 4) * 0.4 + GS2[0] * 0.6

    Posicao += 1
    Contador += 1

Nota_Final = (Media_1*0.4 + Media_2*0.6)

print(f"\nA nota final é : {Nota_Final:.1f}")