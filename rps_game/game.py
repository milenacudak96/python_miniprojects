import random

user_action = int(input('enter a number 0-2:'))

computer_action = random.randint(0, 2)


def get_hand(user_action):
    if user_action == 0:
        print('scissors')
    elif user_action == 1:
        print('rock')
    else:
        print('paper')



person = get_hand(user_action)
computer= get_hand(computer_action)


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


determine_winner(person, computer)
