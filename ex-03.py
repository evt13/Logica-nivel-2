#3) Os pares de instruções abaixo produzem o mesmo resultado? Imprima os valores abaixo, veja se algum deles (A, B ou C) possuem valores diferentes nas versões 1 e 2, e caso sim, explique num comentário o motivo.
Intuito do exercício: O desafio proposto por este exercício é que o aluno entenda se os valores do lado esquerdo e direito dão os mesmo resultados ou não e, quando diferentes, qual a razão de chegar nesse resultado.

A1 ← (4/2)+(2/4)	e	A2 ← 4/2+2/4
B1 ← 4/(2+2)/4	e	B2 ← 4/2+2/4
C1 ← (4+2)*2-4	e	C2 ← 4+2*2-4

A1 = (4/2)+(2/4)
print ("A1=",A1)
B1 = 4/(2+2)/4
print ("B1=",B1)
C1 = (4+2)*2-4
print ("C1=",C1)
A2 = 4/2+2/4
print ("A2=",A2)
B2 = 4/2+2/4
print ("B2=",B2)
C2 = 4+2*2-4
print ("C2=",C2)
# OS PARENTESES VÃO DIZER A ORDEM E A PRIORIDADE DA EQUAÇÃO#
