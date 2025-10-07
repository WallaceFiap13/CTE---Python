# Wallace Queiroz de Lima - RM566217

Avaliacao = ["CP1","CP2","CP3", "Sprint1", "Sprint2", "GS"]  # Lista para as atividades

Notas = {              # Dicionário para armazenar notas
    "CPs_1Sem" : [],
    "CPs_2Sem" : [],
    "CSs_1Sem" : [],
    "CSs_2Sem" : [],
    "GSs" : []
}

Materia = input("\nInsira o nome da 'matéria' que deseja calcular a nota = ")  # Input da matéria

for y in range(2):     # For do semestre
    if y == 0:         # 1° Semestre
        print(f"\n1º Semestre")

        for x in Avaliacao:
            while True:
                Nota = float(input(f"\nInsira a nota do(a) {x} = "))
                if Nota >= 0 and Nota <= 10:  # Restringe a nota inserida estar entre 0 e 10
                    break
                else:
                    print("Input incorreto - a nota deve estar entre 0 e 10 - tente novamente")
            
            if Avaliacao.index(x) < 3:
                Notas["CPs_1Sem"].append(Nota)
            elif Avaliacao.index(x) < 5:
                Notas["CSs_1Sem"].append(Nota)
            else:
                Notas["GSs"].append(Nota)

        Media_1 = (((sum(Notas["CPs_1Sem"]) - min(Notas["CPs_1Sem"])) + sum(Notas["CSs_1Sem"])) / 4) * 0.4 + Notas["GSs"][0] * 0.6   # Calcula a média do 1° Semestre
        
    elif y == 1:      # 2° Semestre
        print(f"\n2º Semestre")

        for x in Avaliacao:
            while True:
                Nota = float(input(f"\nInsira a nota do(a) {x} = "))
                if Nota >= 0 and Nota <= 10:  # Restringe a nota inserida estar entre 0 e 10
                    break
                else:
                    print("Input incorreto - a nota deve estar entre 0 e 10 - tente novamente")

            if Avaliacao.index(x) < 3:
                Notas["CPs_2Sem"].append(Nota)
            elif Avaliacao.index(x) < 5:
                Notas["CSs_2Sem"].append(Nota)
            else:
                Notas["GSs"].append(Nota)

        Media_2 = (((sum(Notas["CPs_2Sem"]) - min(Notas["CPs_2Sem"])) + sum(Notas["CSs_2Sem"])) / 4) * 0.4 + Notas["GSs"][1] * 0.6   # Calcula a média do 2° Semestre
        
        
Nota_Final = (Media_1*0.4 + Media_2*0.6)

frequencia = int(input(f"\nInsira a frequência da matéria '{Materia}' (em porcentagem) = "))

print(f"\nA nota final é : {Nota_Final:.1f}")

if Nota_Final >= 6 and frequencia >= 75:
    print(f"\nSua situação na matéria '{Materia}' é = Aprovado")

elif Nota_Final <6 and Nota_Final >=4 and frequencia >= 75:
    print(f"\nSua situação na matéria '{Materia}' é = Exame")

else:
    print(f"\nSua situação na matéria '{Materia}' é = Reprovado")