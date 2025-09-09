estoque = {"tomate": [1000, 2.3], "alface": [500, 0.45], "batata": [2001, 1.2], "feijão": [100, 1.5]}

venda = [["tomate", 5], ["batata", 10], ["alface", 5]]

total = 0

for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto}: {quantidade} x {preco} = {custo}")
    estoque[produto][0] -= quantidade
    total += custo

print(f"Custo total: {total}")

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: R$ {dados[1]}")



Curso = {"Administração" : ["R$ 2.500,00", "2 Anos", 50] , "Mecatronica" : ["R$ 3.000,00", "4 Anos", 40], "Relações Contábeis" : ["R$ 3.000,00", "2 Anos", 30]}

while True:
    Pesquisa = input("\nDigite o nome do Curso que quer pesquisar na FIAP ('Fim' para terminar)\n").lower() # Traduz o input para menusculo para facilitar comparações
    if Pesquisa == "Fim":
        break
    elif Pesquisa in Curso:
        print(f"Valor = {Curso[Pesquisa][0]} // Período = {Curso[Pesquisa][1]}")
    else:
        print("Curso não encontrado")