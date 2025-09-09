alunos = {"566217" : ["Wallace", "1ECR"], "565540": ["Anna", "1ECR"]} # Chave - valor unico (não pode ter mais valores iguais a ele) // Demais itens - valores variados
print(alunos)

alunos["565540"][0] = "Ana" # Substituir um valor dentro de uma chave específica em um índice específico
print(alunos)

print(alunos["565540"])

print("566217" in alunos) # Consulta para verificar se a chave está na tabela

print(alunos.keys()) # Retorna somente as chaves do dicionário

print(alunos.values()) # Retorna os dados/ valores do dicionário

del alunos["565540"] # Função de Delete
print(alunos)