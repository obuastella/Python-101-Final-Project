# Python101 Final Project
import random
while True:
    correct_answer = random.choice(["rock", "paper", "scissors"])
    user_guess = input("Rock, Paper, Scissors? ").lower()
    if user_guess == correct_answer:
        print("Yay you won!")
        break
    else:
        print("Wrong try again!")
        print(f"The Correct answer was: {correct_answer.upper()}")
