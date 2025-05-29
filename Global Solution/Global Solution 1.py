<<<<<<< HEAD
# Link do Vídeo acelerado para caber em 3min - https://youtu.be/Of2EfVnZoaU
# Link do Vídeo completo 5min 30s - https://youtu.be/aACt7kn6_xw
# Link do Vídeo de teste do código - https://youtu.be/BZj5Y-UBUAc
=======
# Link do Vídeo - 
>>>>>>> f2cc8a3777bc47510b66b5a8835d5e0b4fe1d75a
# Wallace Queiroz de Lima - RM566217

# Contadores
n_leituras = 0
ordem = 0
leitura_critica = 0
i = 0
f = 0
d = 0
acrescimo = 0
decrescimo = 0


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

# Introdução ao Usuário
print("\n========================================")
print("  Detecção de Padrões Sonoros Críticos  ")
print("========================================")
print("Este sistema irá receber as leituras dos sensores")
print("e identificar padrões de risco sonoro.")

# Leitura de Dados
n_leituras = int(input("\nInsira a quantidade de leituras realizadas pelos sensores\n"))

while n_leituras > 0 :
    ordem += 1

    in_intensidade = int(input(f"\nInsira a {ordem}° medição da Intensidade Sonora do ruído, em dB (decibéis)\n"))
    in_frequencia = int(input(f"\nInsira a {ordem}° medição de Frequência do ruído, em Hz (Hertz)\n"))
    in_duracao = int(input(f"\nInsira a {ordem}° medição da Duração do ruído, em s (segundos)\n"))

# Condições Críticas e Emissão de Alertas
    if (in_intensidade > 110) or (in_frequencia > 2 and in_frequencia < 10) or (in_duracao > 10):
        print("\n----------------------------------------")
        print("ALERTA: PADRÃO SONORO CRÍTICO DETECTADO!")
        print("----------------------------------------")
        leitura_critica += 1
    else:
        print("\n----------------------------------------")
        print("Nenhuma anomalia sonora detectada.")
        print("----------------------------------------")

    intensidade.append(in_intensidade)
    frequencia.append(in_frequencia)
    duracao.append(in_duracao)
    
    n_leituras -= 1


# Médias
    # Média da Intensidade Sonora
while i < len(intensidade):
    soma_intensidade += intensidade[i]
    i += 1
md_intensidade = soma_intensidade/len(intensidade)

    # Média da Frequência Sonora
while f < len(frequencia):
    soma_frequencia += frequencia[f]
    f += 1
md_frequencia = soma_frequencia/len(frequencia)

    # Média da Duração Sonora
while d < len(duracao):
    soma_duracao += duracao[d]
    d += 1
md_duracao = soma_duracao/len(duracao)


# Desvio padrão
    # Zerar os contadores
i = 0
f = 0
d = 0

    # Desvio padrão da Intensidade Sonora
while i < len(intensidade):
    somaq_intensidade += ((intensidade[i] - md_intensidade) ** 2)
    i += 1
dp_intensidade = ((somaq_intensidade/len(intensidade)) ** (1/2))

    # Desvio padrão da Frequência Sonora
while f < len(frequencia):
    somaq_frequencia += ((frequencia[f] - md_frequencia) ** 2)
    f += 1
dp_frequencia = ((somaq_frequencia/len(frequencia)) ** (1/2))

    # Desvio padrão da Duração Sonora
while d < len(duracao):
    somaq_duracao += ((duracao[d] - md_duracao) ** 2)
    d += 1
dp_duracao = ((somaq_duracao/len(duracao)) ** (1/2))

    # Estatísticas
print("")
print("\n========================================")
print("          Estatísticas Gerais           ")
print("========================================")

print("\n---------- Intensidade Sonora ----------")
print(f"Média         : {md_intensidade:.2f} dB")
print(f"Desvio Padrão : {dp_intensidade:.2f} dB")

print("\n---------- Frequência Sonora -----------")
print(f"Média         : {md_frequencia:.2f} Hz")
print(f"Desvio Padrão : {dp_frequencia:.2f} Hz")

print("\n----------- Duração do Ruído -----------")
print(f"Média         : {md_duracao:.2f} s")
print(f"Desvio Padrão : {dp_duracao:.2f} s\n")


# Estado Geral do Ambiente
total_leituras = len(intensidade)
porcentagem_critica = ((leitura_critica/total_leituras) * 100)

print("\n========================================")
print("        Estado Geral do Ambiente        ")
print("========================================")

if porcentagem_critica > 40:
    print("\nEstado Geral: RISCO ELEVADO\n")
else:
    print("\nEstado Geral: Monitoramento Normal\n")


# Análise Histórica
    # Ajusta Contadores
i = 1
f = 1
d = 1

    # Máximos e Mínimos da Intensidade Sonora
max_intensidade = intensidade[0]
min_intensidade = intensidade[0]

while i < len(intensidade):
    if intensidade[i] > max_intensidade:
        max_intensidade = intensidade[i]
    if intensidade[i] < min_intensidade:
        min_intensidade = intensidade[i]
    i += 1

    # Máximos e Mínimos da Frequência Sonora
max_frequencia = frequencia[0]
min_frequencia = frequencia[0]

while f < len(frequencia):
    if frequencia[f] > max_frequencia:
        max_frequencia = frequencia[f]
    if frequencia[f] < min_frequencia:
        min_frequencia = frequencia[f]
    f += 1

    # Máximos e Mínimos da Duração Sonora
max_duracao = duracao[0]
min_duracao = duracao[0]

while d < len(duracao):
    if duracao[d] > max_duracao:
        max_duracao = duracao[d]
    if duracao[d] < min_duracao:
        min_duracao = duracao[d]
    d += 1

print("\n========================================")
print("    Análise Histórica dos Parâmetros    ")
print("========================================")

print("\n---------- Intensidade Sonora ----------")
print(f"Máximo : {max_intensidade} dB")
print(f"Mínimo : {min_intensidade} dB")

print("\n---------- Frequência Sonora -----------")
print(f"Máximo : {max_frequencia} Hz")
print(f"Mínimo : {min_frequencia} Hz")

print("\n----------- Duração do Ruído -----------")
print(f"Máximo : {max_duracao} s")
print(f"Mínimo : {min_duracao} s\n")

    # Ajusta Contadores
i = 1

    # Tendencia da Intensidade Sonora
while i < len(intensidade):
    if intensidade[i] > intensidade[i - 1]:
        acrescimo += 1
    elif intensidade[i] < intensidade[i - 1]:
        decrescimo += 1
    i += 1

print("\n========================================")
print("    Tendência de Intensidade Sonora     ")
print("========================================")

if acrescimo > decrescimo:
    print("\nTendência de ALTA na Intensidade Sonora\n")
elif decrescimo > acrescimo:
    print("\nTendência de BAIXA na Intensidade Sonora\n")
else:
    print("\nTendência ESTÁVEL ou OSCILANTE na Intensidade Sonora\n")