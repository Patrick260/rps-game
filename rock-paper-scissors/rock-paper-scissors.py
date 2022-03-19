import random


def play():
    player_action = input("Rock, paper or scissors? ")
    computer_action = random.Random().randint(0, 2)
    if is_valid(player_action):
        result(action_to_num(player_action), computer_action)
    else:
        print(player_action + " isn't a known action!")
        play()


def result(action1, action2):
    if (action1 + 1) % 3 == action2:
        print("Computer played " + str(num_to_action(action2)) + "... You lose!")
    elif action1 == action2:
        print("Computer played " + str(num_to_action(action2)) + "... It's a draw!")
    else:
        print("Computer played " + str(num_to_action(action2)) + "... You win!")


def action_to_num(action):
    if action == "rock" or action == "Rock":
        return 0
    elif action == "paper" or action == "Paper":
        return 1
    elif action == "scissors" or action == "Scissors":
        return 2


def num_to_action(num):
    if num == 0:
        return "rock"
    elif num == 1:
        return "paper"
    elif num == 2:
        return "scissors"


def is_valid(input):
    if input != "rock" and input != "Rock" and input != "paper" and input != "Paper" and input != "scissors" \
            and input != "Scissors":
        return False
    else:
        return True


if __name__ == "__main__":
    while True:
        play()
