import random

def play():
    welcome_mensage()

    secret_word = loading_words_database()
    right_letters = init_right_letters(secret_word)
    print(right_letters)

    hanged = False
    won = False
    mistakes = 0

    while (not hanged and not won):
        shot = ask_letter()

        if (shot in secret_word):
            print("Você acertou, a letra {} pertence a palavra.".format(shot))
            mark_right_letter(shot, right_letters, secret_word)
        else:
            mistakes = mistakes + 1
            print("Você chutou errado! Você ainda pode errar {} vezes.".format(7 - mistakes))
            draw_hang_man(mistakes)

        hanged = mistakes == 7
        won = "_" not in right_letters
        print(right_letters)

    if (hanged):
        print_loser_mensage(secret_word)
    else:
        print_winner_mensage(secret_word)


def welcome_mensage():
    print("--------------------------------")
    print("Bem vindo ao jogo de Forca")
    print("--------------------------------")


def loading_words_database():
    # ou usar essa sintaxe do python (with):
    # with open("palavras.txt") as arquivo:
    #     for linha in arquivo:
    #         linha = linha.strip()
    #         palavras.append(linha)

    words = []
    file = open("palavras.txt", "r")
    for line in file:
        line = line.strip()
        words.append(line)
    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def init_right_letters(word):
    return ["_" for letter in word]


def ask_letter():
    shot = input("Qual a letra? ")
    shot = shot.strip().upper()
    return shot


def mark_right_letter(shot, right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (shot == letter):
            right_letters[index] = letter
        index = index + 1



def draw_hang_man(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_loser_mensage(secret_word):
    print("Você foi enforcado! A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("Fim de jogo!")


def print_winner_mensage(secret_word):
    print("Sim! A palavra correta é {}. Parabéns, você acertou e se livrou da forca.".format(secret_word))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("Fim de jogo!")


if (__name__ == "__main__"):
    play()
