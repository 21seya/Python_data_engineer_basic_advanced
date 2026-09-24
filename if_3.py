"""
Eu cheguei atrasado na aula.Ainda posso entrar ? 

se for a primeira ou segunda vez que você chega atrasado ,pode sim 
Mas se for a terceira vez , você será suspenso.
"""
atrasados = input("Quantas faltas você tem:")

atrasados = 0 
if atrasados >= 3:
    print("você está suspenso!")
elif atrasados == 2:
    print("mais uma falta estará suspenso!")

elif atrasados == 1:
    print("mais duas faltas e estará suspenso!")
else:
    print("pode entrar!")    

