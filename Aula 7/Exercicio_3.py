<<<<<<< HEAD
list_cursos = {"Administração" : [2500.00, "2 Anos", 50] , "Mecatrônica" : [3000.00, "4 Anos", 40], "Relações Contábeis" : [3000.00, "2 Anos", 30]} # Dicionário

vagas_ocp = [["Administração", 10], ["Mecatrônica", 5], ["Relações Contábeis", 15]] # Lista

receita = 0 # Contador

# for vagas_att in vagas_ocp:         // Caso eu precise aproveitar o valor da lista completa
#     curso, qts_vagas = vagas_att    // utilizo a sentença do for assim

for curso, qts_vagas in vagas_ocp: # Senão, assim acaba sendo mais direto.
    print(f"\n{curso} -> {qts_vagas} x {list_cursos[curso][0]} = {qts_vagas * list_cursos[curso][0]}") # Curso -> Vagas Ocupadas x Valor do Curso = Receita por Curso
    
    list_cursos[curso][2] -= qts_vagas # Subtrai a quantidade de vagas ocupadas das vagas iniciais
    
    receita += (qts_vagas * list_cursos[curso][0]) # Adiciona o valor de receita por curso calculado em cara passada do For

print(f"\nReceita parcial total = {receita}")

for chave, dados in list_cursos.items(): # .items() retorna o par chave-dado/valor dentro das variáveis
    print(f"\nCurso: {chave}")
    print(f"Vagas Disponíveis: {dados[2]}")
    print(f"Período: {dados[1]}")
    print(f"Valor da Mensalidade: R$ {dados[0]}")
=======
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