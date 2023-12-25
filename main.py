rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
import sys

choice = ["rock", "paper", "scissors"]

con = 'y'

while con.lower() == "y":
    user_input = input("What is your choice? rock, paper, scissors: ")
    computer = random.choice(choice)

    if user_input.lower() == "rock" and computer == "scissors":
        print("You chose:")
        print(rock)
        print(f"Computer chose:\n{scissors}")
        print("You win!")
    elif user_input.lower() == 'scissors' and computer == "paper":
        print("You chose:")
        print(scissors)
        print(f"Computer chose:\n{paper}")
        print("You win!")
    elif user_input.lower() == "paper" and computer == "rock":
        print("You chose:")
        print(paper)
        print(f"Computer chose:\n{rock}")
        print("You win!")
    else:
        print(f"You chose: {user_input} and computer chose: {computer}")
        print("You lose!")

    con = input("Do you want to continue? y/n? : ")
    if con.lower() == "n":
        print("Thanks for playing!")
        sys.exit()
