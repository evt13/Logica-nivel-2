#) Escreva um algoritmo para ler um valor numérico (do teclado) e escrever (na tela) o seu antecessor

numero = int(input("Digite um número: "))
antecessor = numero - 1
print(f"O antecessor de {numero} é {antecessor}.")

#A função f que você está vendo é uma f-string (ou string formatada) no Python. 
Ela foi introduzida no Python 3.6 e é uma maneira moderna e eficiente de incluir expressões dentro de strings.
O f antes das aspas indica que a string será formatada e permitirá a inserção de variáveis ou expressões diretamente dentro da string,
sem a necessidade de concatenar ou usar placeholders.
