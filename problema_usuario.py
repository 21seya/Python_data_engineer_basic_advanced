usuario = ''
senha = ''
tentativas = 0

while (usuario != 'renan' and senha != 'senha123') and tentativas <3:
    usuario = input("Digite sua senha:")
    tentativas += 1 

if usuario != "renan" and senha != 'senha123':
    print("aguarda uns 30 minutos para digitar novamente!")
else:
    print("Login realizado com sucesso!")
        


