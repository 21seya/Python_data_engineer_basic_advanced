"""
Você trabalha em um sistema que precisa verificar se todas as senhas 
digitadas por usuários são válidas
"""

senhas = ["abc","segura123","12345","python123","oi"]
for senha in senhas:
    if len(senha) >= 6:
        print(f"A senha {senha} e valida")
    else:
        print(f"A senha {senha} não e valida")
            