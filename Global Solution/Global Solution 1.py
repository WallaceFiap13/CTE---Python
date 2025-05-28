
# Contadores
n_leituras = 0
in_intensidade = 0
in_frequencia = 0
in_duracao = 0
ordem = 0
leitura_critica = 0
i = 0
f = 0
d = 0

# Listas
intensidade = []
frequencia = []
duracao = []

# Somadores
soma_intensidade = 0
soma_frequencia = 0
soma_duracao = 0
somaq_intensidade = 0
somaq_frequencia = 0
somaq_duracao = 0


# Lógica Geral
n_leituras = int(input("\nInsira a quantidade de leituras realizadas pelos sensores\n"))

while n_leituras > 0 :

    ordem += 1

    in_intensidade = int(input(f"Insira a {ordem}° medição da Intensidade Sonora do ruído, em dB (decibéis)"))
    in_frequencia = int(input(f"Insira a {ordem}° medição de Frequência do ruído, em Hz (Hertz)"))
    in_duracao = int(input(f"Insira a {ordem}° medição da Duração do ruído, em s (segundos)"))

    if (in_intensidade > 110) or (in_frequencia > 2 and in_frequencia < 10) or (in_duracao > 10):
        print("Alerta: Padrão sonoro crítico detectado!")
        leitura_critica += 1
    else:
        print("Nenhuma anomalia sonora detectada.")

    intensidade.append(in_intensidade)
    frequencia.append(in_frequencia)
    duracao.append(in_duracao)
    
    n_leituras -= 1

# Médias
while i < len(intensidade):
    soma_intensidade += intensidade[i]
    i += 1
md_intensidade = soma_intensidade/len(intensidade)

while f < len(frequencia):
    soma_frequencia += frequencia[f]
    f += 1
md_frequencia = soma_frequencia/len(frequencia)

while d < len(duracao):
    soma_duracao += duracao[d]
    d += 1
md_duracao = soma_duracao/len(duracao)

# Zerar os contadores
i = 0
f = 0
d = 0

# Desvio padrão
while i < len(intensidade):
    somaq_intensidade += ((intensidade[i] - md_intensidade) ** 2)
    i += 1
dp_intensidade = ((somaq_intensidade/len(intensidade)) ** (1/2))

while f < len(frequencia):
    somaq_frequencia += ((frequencia[f] - md_frequencia) ** 2)
    i += 1
dp_frequencia = ((somaq_frequencia/len(frequencia))) ** (1/2))

while d < len(duracao):
    somaq_duracao += ((duracao[d] - md_duracao) ** 2)
    i += 1
dp_duracao = ((somaq_duracao/len(duracao))) ** (1/2))

# Ajusta Contadores
i = 1
f = 1
d = 1

# Máximos e Mínimos
max_intensidade = intensidade[0]
min_intensidade = intensidade[0]

while i < len(intensidade):
    if intensidade[i] > max_intensidade:
        max_intensidade = intensidade[i]
    if intensidade[i] < min_intensidade:
        min_intensidade = intensidade[i]
    i += 1


# Prints
total_leituras = len(intensidade)
porcentagem_critica = ((leitura_critica/total_leituras) * 100)

if porcentagem_critica > 40:
    print("Estado Geral: Risco Elevado")
else:
    print("Estado Geral: Monitoramento Normal")

print(f"{md_intensidade}")
print(f"{md_frequencia}")
print(f"{md_duracao}")

print(f"{dp_intensidade}")
print(f"{dp_frequencia}")
print(f"{dp_duracao}")