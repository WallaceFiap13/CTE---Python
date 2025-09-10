list_cursos = {
    "Administração" : [2500.00, "2 Anos", 50] ,
    "Mecatrônica" : [3000.00, "4 Anos", 40],
    "Relações Contábeis" : [3000.00, "2 Anos", 30]
    } # Dicionário

receita = 0 # Contador

for curso, dados in list_cursos.items():
    print(f"\nCurso - {curso} // Vagas Disponíveis - {dados[2]} // Período: {dados[1]} // Valor da Mensalidade: R$ {dados[0]}")
    vagas_ocupadas = int(input("Quantas vagas desse curso foram ocupadas?\n"))

    list_cursos[curso][2] -= vagas_ocupadas # Subtrai a quantidade de vagas ocupadas das vagas iniciais

    receita += (vagas_ocupadas * list_cursos[curso][0]) # Adiciona o valor de receita por curso calculado em cara passada do For

print(f"\nReceita parcial total = {receita}")

for chave, dados in list_cursos.items(): # Situação final dos cursos
    print(f"\nCurso: {chave}")
    print(f"Vagas Disponíveis: {dados[2]}")
    print(f"Período: {dados[1]}")
    print(f"Valor da Mensalidade: R$ {dados[0]}")