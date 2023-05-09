"""
Usuário vai escolher uma das 3 opções e vai ser escolher um valor aleatório

"""
import random 

user_points = 0
computer_points = 0


options = ["r", "t", "p"]


while True:
    user_choice = input("\n R(Pedra) \n T(Tesoura) \n P(Papel) \n Q para sair. \n Escolha: ").lower()
    
    if user_choice == 'q':
        break

    if user_choice not in options:
        continue

    comp_choice = random.randint(0, 2)

    compu_options = options[comp_choice]

    print(f"O computador escolheu: {compu_options}" )

    if user_choice == compu_options:
        print("Empate!")

    elif user_choice == "r" and compu_options == "t":
        print("Você ganhou!")
        user_points = user_points + 1

    elif user_choice == "p" and compu_options == "r":
        print("Você ganhou!")
        user_points = user_points + 1

    elif user_choice == "t" and compu_options == "p":
        print("Você ganhou!")
        user_points = user_points + 1