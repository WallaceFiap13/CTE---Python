salario = float(input("\nInsira o seu salário: "))

if salario > 1250:
    print(f"\nSeu salário foi para = R${salario+salario*0.1}0")

if salario <= 1250:
    print(f"\nSeu salário foi para = R${salario+salario*0.15}0")