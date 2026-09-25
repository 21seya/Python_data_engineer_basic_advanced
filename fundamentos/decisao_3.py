distancia_gol = 20

if distancia_gol < 18:
    print("Entrou na área. Perigo de gol!")
else:
    print("Não entrou na área.")    

forca_do_chute = 86 
reflexo_goleiro = 90 

if forca_do_chute > reflexo_goleiro:
    print("Gol!")
else:
    print("Goleiro defendeu!")    