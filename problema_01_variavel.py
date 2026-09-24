# problema 1 - valor por hora 
#Escreva um programa que retorna o valor por hora de um funcionário 
# com base no seu salário mensal e horas trabalhadas por mês

salario_mensal=input("Qual é o seu salário mensal:")
horas_trabalhadas = input("Quantas horas trabalhada por mês:")
valor_hora = float(salario_mensal) / int(horas_trabalhadas)
print(valor_hora)

