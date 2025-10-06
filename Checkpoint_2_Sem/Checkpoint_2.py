Avaliacao = ["CP1","CP2","CP3", "Sprint1", "Sprint2", "GS"]  # Lista para loop

Notas = {              # Dicionário para armazenar notas
    "CPs_1Sem" : [],
    "CPs_2Sem" : [],
    "CSs_1Sem" : [],
    "CSs_2Sem" : [],
    "GSs" : []
}

Contador = 1 # COntador para auxiliar no loop

while Contador < 3:
    if Contador == 1:
        print("\n1° Semestre")
    
    if Contador == 2:
        print("\n2° Semestre")
        
    for x in Avaliacao:
        
        while True:
            Nota = float(input(f"\nInsira a nota do(a) {x} = "))
            if Nota >= 0 and Nota <= 10:  # Restringe a nota inserida estar entre 0 e 10
                break
            else:
                print("Input incorreto - a nota deve estar entre 0 e 10 - tente novamente")
        
        if Contador == 1:                 # Indicia primeiro semestre
            if Avaliacao.index(x) < 3:
                Notas["CPs_1Sem"].append(Nota)
            elif Avaliacao.index(x) < 5:
                Notas["CSs_1Sem"].append(Nota)
            else:
                Notas["GSs"].append(Nota)

        elif Contador == 2:               # Indicia segundo semestre
            if Avaliacao.index(x) < 3:
                Notas["CPs_2Sem"].append(Nota)
            elif Avaliacao.index(x) < 5:
                Notas["CSs_2Sem"].append(Nota)
            else:
                Notas["GSs"].append(Nota)

    if Contador == 1:        # Calculo da média do primeiro semestre
        Media_1 = (((sum(Notas["CPs_1Sem"]) - min(Notas["CPs_1Sem"])) + sum(Notas["CSs_1Sem"])) / 4) * 0.4 + Notas["GSs"][0] * 0.
        
    elif Contador == 2:     # Calculo da média do segundo semestre
        Media_2 = (((sum(Notas["CPs_2Sem"]) - min(Notas["CPs_2Sem"])) + sum(Notas["CSs_2Sem"])) / 4) * 0.4 + Notas["GSs"][1] * 0.6

    Contador += 1

Nota_Final = (Media_1*0.4 + Media_2*0.6)

print(f"\nA nota final é : {Nota_Final:.1f}")