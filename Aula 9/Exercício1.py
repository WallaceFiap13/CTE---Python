from Funções_ex1_2 import * # se colocar o nome específico da função ele importa uma função só

operacao = input("Escolha a operação a se fazer (soma, subtracao, multiplicacao, divisao) = ")
n1 = float(input("Insira o 1° Número = "))
n2 = float(input("Insira o 2° Número = "))

if operacao == "soma":
    print(soma(n1, n2))
elif operacao == "subtracao":
    print(subtracao(n1, n2))
elif operacao == "multiplicacao":
    print(multiplicacao(n1, n2))
elif operacao == "divisao":
    print(divisao(n1, n2))
else:
    print("Operação inválida!")