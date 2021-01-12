from random import randint

def main():
    jogo = input("Qual o jogo? (C -> Cara/Coroa ou H -> Higher/Lower) ")
    print("\n")

    while jogo.lower() not in ["c", "h"]:
        jogo = input("Qual o jogo? (C -> Cara/Coroa ou H -> Higher/Lower) ")
        print("\n")

    if jogo.upper() == "C":
        ganho, perdido = CaraCoroa()

        print(f"Voce ganhou {ganho} jogos e perdeu {perdido}\n")
        if ganho > perdido:
            print("Você ganhou!\n")
        else:
            print("O PC ganhou!\n")

    else:
        HigherLower()


def CaraCoroa():
    ganho, perdido, i = 0, 0, 1

    jogada = int(input("Quantas jogadas você quer fazer? "))
    while i <= jogada:
        escolha = input("Cara ou Coroa? ")
            
        while escolha.lower() not in ["cara", "coroa"]:
            print("Tente de novo!")
            escolha = input("Cara ou Coroa? ")
            print("\n")
            
        if escolha.lower() == "cara":
            x = 1
                
        else:
            x = 2
        
        jogo = randint(1, 2) # Escolhe se cara ou coroa
        
        if jogo == x:
            print("Deu", escolha.capitalize(), "Você ganhou!\n")
            ganho += 1
        else:
            perdido += 1
            print("Deu", escolha.capitalize(), "Você perdeu!\n")    
        
        i += 1 
    return ganho, perdido

def HigherLower():
    pass


main()
