# Wallace Queiroz de Lima - RM566217 #
# Matheus Martins Porto - RM561847 #

n = 1 # Contador
md1 = 0 # Somador
md2 = 0 # Somador

print("\n------------------------------------------")
print("\nPara saber sua Média Anual, digite suas seguintes notas:")
print("\n------------------------------------------")
print("------------------------------------------")

while n <= 2:
    if n == 1:
        print("\n 1° Semestre")
        print("\n------------------------------------------")
        checkpoint1 = float(input("\nCheckpoint 1 (de 0 a 10) = "))
        checkpoint2 = float(input("\nCheckpoint 2 (de 0 a 10) = "))
        checkpoint3 = float(input("\nCheckpoint 3 (de 0 a 10) = "))

        print("\n------------------------------------------")

        sprint1 = float(input("\nSprint 1 (de 0 a 10) = "))
        sprint2 = float(input("\nSprint 2 (de 0 a 10) = "))

        print("\n------------------------------------------")

        gs = float(input("\nGlobal Solution (de 0 a 10) = "))

        print("\n------------------------------------------")
        print("------------------------------------------")

        if checkpoint1 <= checkpoint2 and checkpoint1 <= checkpoint3:
            soma_checkpoints = checkpoint2 + checkpoint3
        elif checkpoint2 <= checkpoint1 and checkpoint2 <= checkpoint3:
            soma_checkpoints = checkpoint1 + checkpoint3
        else:
            soma_checkpoints = checkpoint1 + checkpoint2

        md1 = ((((soma_checkpoints) + (sprint1+sprint2))/4)*0.4) + (gs*0.6)

        n +=1
   
    if n == 2:
        

        print("\n 2° Semestre")
        print("\n------------------------------------------")
        checkpoint1 = float(input("\nCheckpoint 1 (de 0 a 10) = "))
        checkpoint2 = float(input("\nCheckpoint 2 (de 0 a 10) = "))
        checkpoint3 = float(input("\nCheckpoint 3 (de 0 a 10) = "))

        print("\n------------------------------------------")

        sprint1 = float(input("\nSprint 1 (de 0 a 10) = "))
        sprint2 = float(input("\nSprint 2 (de 0 a 10) = "))

        print("\n------------------------------------------")

        gs = float(input("\nGlobal Solution (de 0 a 10) = "))

        print("\n------------------------------------------")
        print("------------------------------------------")

        if checkpoint1 <= checkpoint2 and checkpoint1 <= checkpoint3:
            soma_checkpoints = checkpoint2 + checkpoint3
        elif checkpoint2 <= checkpoint1 and checkpoint2 <= checkpoint3:
            soma_checkpoints = checkpoint1 + checkpoint3
        else:
            soma_checkpoints = checkpoint1 + checkpoint2

        md2 = ((((soma_checkpoints) + (sprint1+sprint2))/4)*0.4) + (gs*0.6)

        n +=1

print(f"\nSua Média do 1° Semestre é = {md1:.1f}")
print(f"\nSua Média do 2° Semestre é = {md2:.1f}")
print(f"\nSua Média Anual é = {(md1*0.4)+(md2*0.6):.1f}\n")

print("------------------------------------------\n")