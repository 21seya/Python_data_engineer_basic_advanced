gols_brasil = 0

for lance in range(1,6):
    print(f"Lance perigoso,número {lance}")

    resultado = input("Foi gol do Brasil? Digite sim ou não: ")

    if resultado == "sim":
        gols_brasil += 1
        print("GOOOOL!")
    else:
        print("Não foi gol")

print("Fim de Jogo!")

print(f"Total de gols do Brasil: {gols_brasil}")