vcasa = float(input("\nQual o valor do Imóvel, em reais? "))
salario = float(input("\nQual o seu salário atualmente, em reais? "))
anos = int(input("\nQual a quantidade de anos do empréstimo? "))

vprestacao = vcasa / (anos * 12)

if vprestacao < (0.3 * salario):
    print(f"\nSua prestação é de R$ {vprestacao:.2f}")
else:
    print("\nSua prestação é superior a 30% do seu salário.")