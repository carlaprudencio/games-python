import guess_the_number
import hang_man

def menu():
    print("--------------------------------")
    print("Bem vindo! Escolha seu jogo!")
    print("--------------------------------")

    print("1 - Adivinhação, 2 - Forca")
    chosen_game = int(input("Digite o número do jogo escolhido: "))


    if(chosen_game == 1):
        print("Jogo escolhido: Adivinhação")
        guess_the_number.play()
    elif(chosen_game == 2):
        print("Jogo escolhido: Forca")
        hang_man.play()

if(__name__ == "__main__"):
    menu()
