#Rock,Paper and Scissor Game

import random

def show_menu():
    print("\n--- Rock, Paper, Scissors Game ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ["Rock", "Paper", "Scissors"]

    while True:
        show_menu()
        try:
            user_input = int(input("Enter your choice (1-4): "))
            if user_input == 4:
                print("Thank you for playing! Goodbye!")
                break

            if user_input < 1 or user_input > 4:
                print("Invalid choice! Please select a valid option.")
                continue

            player_choice = choices[user_input - 1]
            computer_choice = random.choice(choices)

            print(f"\nYou chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            result = determine_winner(player_choice, computer_choice)
            print(f"Result: {result}")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
