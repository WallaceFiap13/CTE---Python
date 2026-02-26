distancia = int(input("\nQual a distância, em Km, que você deseja percorrer?\n"))

if distancia < 200:
    print(f"\nA sua passagem será no valor de = R$ {distancia * 0.5}0\n")

if distancia >= 200:
    print(f"\nA sua passagem será no valor de = R$ {distancia * 0.45}0\n")