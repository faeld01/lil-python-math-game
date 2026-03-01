import random
import os

vidas = 3
pontos = 0
check = "Go!"

while vidas > 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(check)
    print(f"Pontos {pontos} - Vidas: {vidas}\n")
    if pontos <= 5:
        termo_a = random.randint(0,10)
        termo_b = random.randint(0,10)
    elif 5 < pontos <= 10:
        termo_a = random.randint(10,20)
        termo_b = random.randint(10,20)
    elif 10 < pontos <= 15:
        termo_a = random.randint(10,50)
        termo_b = random.randint(10,50)
    else:
        termo_a = random.randint(10,99)
        termo_b = random.randint(10,99)

    expressao = input(f"{termo_a} + {termo_b} = ")
    resultado = int(expressao)

    if resultado == termo_a + termo_b:    
        check = "Certo!"
        pontos = pontos+1            
    else:
        check = f"Errado! O correto é {termo_a + termo_b}"
        vidas = vidas-1
os.system('cls' if os.name == 'nt' else 'clear')
print(check)   
print(f"Fim de jogo! - Você fez {pontos} pontos!")