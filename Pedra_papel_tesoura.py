"""
Usuário vai escolher uma das 3 opções e vai ser escolher um valor aleatório

"""
import random 

user_points = 0
computer_points = 0


options = ["r", "t", "p"]

options_resultado = ["Pedra", "Tesoura", "Papel"]

while True:
    user_choice = input("\n R(Pedra) \n T(Tesoura) \n P(Papel) \n Q para sair. \n Escolha: ").lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        continue

    comp_choice = random.randint(0, 2)

    compu_options = options[comp_choice]
    options_resultado_ = options_resultado[comp_choice]
    
    print("-" * 20 )
    print(f" O computador escolheu: {options_resultado_}" )

    if user_choice == compu_options:
        print(" Empate!")
        print("-" * 20 )
    elif user_choice == "r" and compu_options == "t":
        print(" Você ganhou!")
        print("-" * 20 )
        user_points = user_points + 1

    elif user_choice == "p" and compu_options == "r":
        print( "Você ganhou!")
        print("-" * 20 )
        user_points = user_points + 1

    elif user_choice == "t" and compu_options == "p":
        print(" Você ganhou!")
        print("-" * 20 )
        user_points = user_points + 1

    else:
        print(" Você perdeu!")
        print("-" * 20 )
        computer_points = computer_points + 1

print("-" * 20 )
print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if computer_points > user_points:
    print("Derrota!!!!")
    print("-" * 20 )
elif computer_points == user_points:
    print("Empate")
    print("-" * 20 )
else:
    print("Vitória!!")
    print("-" * 20 )