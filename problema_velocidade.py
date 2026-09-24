velocidade = float(input("Digite  velocidade:"))
velocidade_maxima = 80 
if velocidade <= velocidade_maxima:
    print('Não houve multa')
elif velocidade <= velocidade_maxima + 10:
    print("Multa leve")
elif velocidade <= velocidade_maxima + 20:
    print("Multa media")
elif velocidade <= velocidade_maxima + 30:
    print("Multa Grave")    
else:
    print("Multa Gravissima")           
