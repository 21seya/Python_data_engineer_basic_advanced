"""
Crie um programa que receba um número e imprima o seu fatorial
"""
numero = int(input("Digite o valor fatorial deseja calcular:"))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1,numero+1):
        print(f"{fatorial} * {item}")
        fatorial= fatorial * item
        print(f"{fatorial}")
    print(f"O fatorial de {numero} e {fatorial}")    
else:
    print("Informar numeros positivos!")
