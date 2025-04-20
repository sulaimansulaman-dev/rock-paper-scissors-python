#Sulaiman Sulaman
#45427429

import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        
        return "You win!"
    
    else:
        
        return "Computer wins!"

# Function to display the choices and the winner
def display_result(player_choice, computer_choice, result):
    print(f"Your choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

# Valid choices
choices = ['rock', 'paper', 'scissors']

play_again = True

while play_again:
    # Player's turn
    player_choice = input("Enter your choice (rock, paper, scissors): ")

    # Validate the player's choice
    while player_choice not in choices:
        print("Invalid choice. Please try again.")
        player_choice = input("Enter your choice (rock, paper, scissors): ")

    # Computer's turn
    computer_choice = random.choice(choices)

    # Determine the winner
    result = determine_winner(player_choice, computer_choice)

    # Display the choices and the result
    display_result(player_choice, computer_choice, result)

    # Ask the player if they want to play again
    play_again_input = input("Do you want to play again? (yes/no): ")
    play_again = play_again_input.lower() == 'yes'
