# Tupla é uma lista que não pode ser modificada

# --------------------------------------------------------------

lista_alunos = ["Guilherme",   # Lista entre []
                "Wallace", 
                "Pedro"]

print(lista_alunos)

lista_alunos.append("Anna")

print(lista_alunos)

# --------------------------------------------------------------

tupla_alunos = ("Guilherme",   # Tupla entre ()
                "Wallace", 
                "Pedro")

print(tupla_alunos)

aluno1, aluno2, aluno3 = tupla_alunos # Desempacotamento

print(aluno1)
print(aluno2)
print(aluno3)

# --------------------------------------------------------------

um_item = ("sla",) # Tem que colocar uma "," para entender que é uma tupla
print(len(um_item))

# --------------------------------------------------------------

# Tranformar lista em tupla

lista_notas = [9, 10, 5, 8]
print(lista_notas)

tupla_notas = tuple(lista_notas)
print(tupla_notas)

# --------------------------------------------------------------

# Soma de tuplas

tupla1 = (1,6,7)
tupla2 = (15,6,8)

tupla3 = tupla1 + tupla2

print(tupla3)

# --------------------------------------------------------------

