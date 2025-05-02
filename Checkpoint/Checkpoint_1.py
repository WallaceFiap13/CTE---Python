# Wallace Queiroz de Lima - RM566217 #

print("\nPara saber sua Média Semestral, digite suas seguintes notas:\n")

checkpoint1 = float(input("Checkpoint 1 (de 0 a 10) = "))
checkpoint2 = float(input("\nCheckpoint 2 (de 0 a 10) = "))
checkpoint3 = float(input("\nCheckpoint 3 (de 0 a 10) = "))

sprint1 = float(input("\nSprint 1 (de 0 a 10) = "))
sprint2 = float(input("\nSprint 2 (de 0 a 10) = "))

gs = float(input("\nGlobal Solution (de 0 a 10) = "))

menorcheck = checkpoint1
if checkpoint2 <= checkpoint1 and checkpoint2 <= checkpoint3:
    menorcheck = checkpoint2
if checkpoint3 <= checkpoint2 and checkpoint3 <= checkpoint1:
    menorcheck = checkpoint3

media = ((((checkpoint1+checkpoint2+checkpoint3-menorcheck) + (sprint1+sprint2))/4)*0.4) + (gs*0.6)

print(f"\nSua Média Semestral é = {media:.1f}")