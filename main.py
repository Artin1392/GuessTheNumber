# moudels
from random import randint, choice

# Welcome and start message
print("Welcome to the GuessTheNumber game.\n")
start_inp = input("Start? (y/n): ")

# Functions

def Cheer():
    cheer_list = ["Well done", "Good job", "Perfect", "Excellent", "Terrific", "Marvelous", "Bravo"]
    return choice(cheer_list)

def help_player():
    return "Help"

def Check_number(real, guess):
    """ This function checks real and guessed number. """
    if guess == real:
        return Cheer()
    if guess != real:
        return help_player()

# Check start input
if start_inp == "y":
   
    print("Game started!\n")
    game = True
    real_number = randint(0, 100) + 1
    print(real_number)
    while game:
        guessed_number = int(input("your number: "))
        check = Check_number(real_number, guessed_number)
        print(check)

elif start_inp == "n":
    
    print("bye")
    quit()
