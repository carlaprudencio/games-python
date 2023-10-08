import random


def play():
    welcome_mensage()

    secret_number = random.randint(1, 100)
    score = 1000

    chosen_level = choose_level()
    total_attempts = define_attempts(chosen_level)

    for round in range(1, total_attempts + 1):
        print("Tentativa {} de {}".format(round, total_attempts))
        shot_str = input("Digite o seu número: ")
        print("Você digitou o número:", shot_str)
        shot = int(shot_str)

        if (shot < 1 or shot > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        won = shot == secret_number
        bigger = shot > secret_number
        smaller = shot < secret_number

        if (won):
            print_winner_mensage(score)
            break
        else:
            if (bigger):
                print("Que pena! Você errou! O seu chute foi maior do que o número secreto.")
                if (round == total_attempts):
                    print_loser_mensage(secret_number, score)
            elif (smaller):
                print("Que pena! Você errou! O seu chute foi menor do que o número secreto.")
                if (round == total_attempts):
                    print_loser_mensage(secret_number, score)

            lost_scores = abs(secret_number - shot)
            score = score - lost_scores


def welcome_mensage():
    print("--------------------------------")
    print("Bem vindo ao jogo de Adivinhação")
    print("--------------------------------")


def choose_level():
    print("Qual o nível de dificuldade desejo?")
    print("1 - Fácil, 2 - Médio, 3 - Díficil")
    chosen_level = int(input("Digite o número do nível escolhido: "))
    print("Você escolheu o nível:", chosen_level)
    return chosen_level


def define_attempts(chosen_level):
    if (chosen_level == 1):
        total_attempts = 20
    elif (chosen_level == 2):
        total_attempts = 10
    else:
        total_attempts = 5
    return total_attempts


def print_winner_mensage(score):
    print("Você acertou e fez {} pontos.".format(score))
    print("Fim de jogo!")


def print_loser_mensage(secret_number, score):
    print("O número secreto era {}. Você fez {} pontos.".format(secret_number, score))
    print("Fim de jogo!")


if (__name__ == "__main__"):
    play()
