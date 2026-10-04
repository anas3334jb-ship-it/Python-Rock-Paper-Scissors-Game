import random

# Display welcome message and instructions to the user
print("--- Welcome to Rock, Paper, Scissors Game ---")
print("Choices available: rock, paper, scissors")

# Taking user input, converting to lowercase, and removing extra whitespace for safety
user_choice = input("Enter your choice: ").strip().lower()

# Define valid choices for the game
valid_choices = ["rock", "paper", "scissors"]

# Input Validation: check if the user entered a valid game option
if user_choice not in valid_choices:
    print("Error: Invalid choice! Please choose rock, paper, or scissors.")
    exit()

# Generate a random choice for the computer using Python's random module
computer_choice = random.choice(valid_choices)
print(f"Computer chose: {computer_choice}")

# Determine the winner using conditional statements (if-elif-else)
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations! You win!")
else:
    print("Computer wins! Better luck next time.")