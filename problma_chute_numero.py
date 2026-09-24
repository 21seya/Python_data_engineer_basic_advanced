"""
Escreva um programa que , ao iniciar , gere um valor 
aleatório de 1 a 10 e permita que usuário chute números 
até acertar o valor gerado.

O programa deve informar se o chute foi maior , ou menor ou igual ao valor aleatório 
gerado no inicio.
"""

import random 

valor_aleatorio = random.randint(1,10)
acertou = False 

while acertou == False:
    chute = int(input('Chute um numero:'))
    if chute > valor_aleatorio:
        print('chute um valor mais baixo')
    elif chute < valor_aleatorio:
        print('chute um valor mais alto')
    else:
        print('Você acertou')
        acertou = True        