# Python101 Final Project
import random
# While loop
while True:
    # Get input from the user
    user_input = input("Choose: rock, paper, scissors: ")
    user_input = user_input.lower()
    print(user_input)
    # If the user wants to quit the game.
    if user_input == "quit":
        print("You have quit the game.")
        break
    # If the user does not input either rock, paper or scissors
    if user_input != 'rock' and user_input != 'paper' and user_input != 'scissors':
        print("Please choose the right option.")
        continue
    # The computer's choice
    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"The computer chose: {computer_answer}")
    if user_input == "rock" and computer_answer == "scissors":
        print("You win!")
        break
    elif user_input == "paper" and computer_answer == "rock":
        print("You win!")
        break
    elif user_input == "scissors" and computer_answer == "paper":
        print("You win!")
        break
    else:
        print("You lost. Try again")
