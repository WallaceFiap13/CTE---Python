#Utilização de inputs variados + formatação de casas decimais

nome = input(("Qual seu nome?"))
peso = float(input("Qual seu peso?"))
altura = float(input("qual sua altura?"))

IMC = (peso / altura**2)

print(f"{nome}, seu IMC é: {IMC:.2f}") 

