vcasa = float(input("Qual o valor do Imóvel, em reais? "))
salario = float(input("Qual o seu salário atualmente, em reais? "))
anos = int(input("Qual a quantidades de anos do empréstimo? "))

vprestacao = vcasa/(anos*12)

if vprestacao < (0.3*salario):
    print("Sua prestação é de {vprestacao}")
    else
        print("Sua prestação é superior à 30% do seu salário")