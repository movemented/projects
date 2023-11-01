import random 
# play rock paper scissors with the computer cuz you got no friends :OOO

user_action = input("Enter (Rock, Paper, Scissors) ")
possible_actions = ["Rock", "Paper", "Scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action} and the computer chose {computer_action}\n")

# Logic

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")

elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")

elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
