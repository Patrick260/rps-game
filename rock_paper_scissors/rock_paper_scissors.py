#    Copyright (C) 2022  Patrick260
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
    if action in ["rock", "Rock"]:
        return 0
    elif action in ["paper", "Paper"]:
        return 1
    elif action in ["scissors", "Scissors"]:
        return 2


def num_to_action(num):
    if num == 0:
        return "rock"
    elif num == 1:
        return "paper"
    elif num == 2:
        return "scissors"


def is_valid(input):
    if input in ["rock", "Rock", "paper", "Paper", "scissors", "Scissors"]:
        return True
    else:
        return False
