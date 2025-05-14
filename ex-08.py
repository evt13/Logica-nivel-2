#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.


salario_mensal=float(input("didgite seu salario:"))
print("salario mensal=R$",salario_mensal)
reajuste=float(input("digite o valor do reajuste:"))
print("Reajuste=",reajuste,"%")
valor_reajustado=(salario_mensal * reajuste/100)
print(f"valor a ser somado ao pagamento=R$: {valor_reajustado:.2f}")
print(f"salario após o reajuste: {valor_reajustado+salario_mensal:.2f}")
