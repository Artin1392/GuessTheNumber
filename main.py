# moudels
from random import randint

# Welcome and start message
print("Welcome to the GuessTheNumber game.\n")
start_inp = input("Start? (y/n): ")


# Check start input
if start_inp == "y":
    
    print("Game started!\n")
    game = True
    real_number = randint(0, 100) + 1
    while game:
        guessed_number = int(input("your number: "))


elif start_inp == "n":
    
    print("bye")
    quit()
