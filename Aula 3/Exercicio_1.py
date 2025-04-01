velocidade_usuario = int(input("\nQual era a sua velocidade quando passou no Radar?\n"))

velocidade_limite = 80

multa = (velocidade_usuario - velocidade_limite)*5

if velocidade_usuario > velocidade_limite :
    print(f"\nVocê foi multado em = R$ {multa},00")

else:
    print("\nVocê não foi multado")