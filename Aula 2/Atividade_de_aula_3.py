#Utilização de inputs variados + formatação de casas decimais

nome = input(("\nQual seu nome?\n"))
peso = float(input("\nQual seu peso? (em Kg)\n"))
altura = float(input("\nQual sua altura? (em m)\n"))

IMC = (peso / altura**2)

print(f"\n{nome}, seu IMC é: {IMC:.2f} kg/m^2\n")

# O "\n" faz pular linha numa formatação de string, seja ela (input) ou (print)
# Pode ser usada no começo ou no final da string para formatar
# Tá do lado esquerdo do teclado