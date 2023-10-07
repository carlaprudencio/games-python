import adivinhacao
import forca

def menu_escolha():
    print("--------------------------------")
    print("Bem vindo! Escolha seu jogo!")
    print("--------------------------------")

    print("1 - Adivinhação, 2 - Forca")
    jogo_escolhido = int(input("Digite o número do jogo escolhido: "))


    if(jogo_escolhido == 1):
        print("Jogo escolhido: Adivinhação")
        adivinhacao.jogar()
    elif(jogo_escolhido == 2):
        print("Jogo escolhido: Forca")
        forca.jogar()

if(__name__ == "__main__"):
    menu_escolha()
