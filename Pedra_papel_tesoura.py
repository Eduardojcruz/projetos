"""
Usuário vai escolher uma das 3 opções e vai ser escolher um valor aleatório

"""
import random 

user_points = 0
computer_points = 0


options = ["r", "t", "p"]


while True:
    user_choice = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        continue

    computer_choice = random.randint(0, 2)