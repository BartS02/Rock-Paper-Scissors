#import random
#from hands import hands

# while True:
#     user_action = input("Enter a choice (rock, paper, scissors): ")
#     possible_actions = ["rock", "paper", "scissors"]
#     computer_action = random.choice(possible_actions)
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")

#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() != "y":
#         break



import random
from hands import hands
 
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
rounds_played = 0
 
while user_wins < 4 and computer_wins < 4:
    user_input = input("Type Rock, Paper, Scissors, or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input in options:
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        print("Computer picked", computer_pick)
        print("You chose:")
        print(hands(user_input))
        print("Computer chose:")
        print(hands(computer_pick))
        if (user_input == "rock" and computer_pick == "scissors") or \
           (user_input == "paper" and computer_pick == "rock") or \
           (user_input == "scissors" and computer_pick == "paper"):
            print("You won!")
            user_wins += 1
        elif user_input == computer_pick:
            print("Tie")
        else:
            print("You lost!")
            computer_wins += 1
        rounds_played += 1
        print("You won", user_wins, "times." )
        print("The computer won", computer_wins, "times.")
        print("Rounds played:", rounds_played)
        print()
 
if user_wins > computer_wins:
    print("Congratulations! You won the best of 7 rounds!")
elif user_wins == computer_wins:
    print("It's a tie!")
else:
    print("The computer won the best of 7 rounds. Better luck next time!")

