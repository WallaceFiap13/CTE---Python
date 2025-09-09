Curso = {"Administração" : ["R$ 2.500,00", "2 Anos"] , "Mecatronica" : ["R$ 3.000,00", "4 Anos"], "Relações Contábeis" : ["R$ 3.000,00", "2 Anos"]}

while True:
    Pesquisa = input("\nDigite o nome do Curso que quer pesquisar na FIAP ('Fim' para terminar)\n").lower() # Traduz o input para menusculo para facilitar comparações
    if Pesquisa == "Fim":
        break
    elif Pesquisa in Curso:
        print(f"Valor = {Curso[Pesquisa][0]} // Período = {Curso[Pesquisa][1]}") # Como especificar um dado/valor específico dentro de uma chave
    else:
        print("Curso não encontrado")