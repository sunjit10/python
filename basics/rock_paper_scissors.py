import random

pick_one = ["rock", "paper", "scissors"]

def get_choices():
    player_choice = input("Enter your choice ")
    computer_choice = random.choice(pick_one)
    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    print(f"You chose {player}, and computer chose {computer}")
    if (player == "rock" and computer == "paper"):
        print("Computer wins")
    elif (player == "rock" and computer == "scissors"):
        print("You win!!!")
    elif (player == "paper" and computer == "rock"):
        print("You win!!!")
    elif (player == "paper" and computer == "scissors"):
        print("Computer wins")
    elif (player == "scissors" and computer == "paper"):
        print("You win!!!")
    elif (player == "scissors" and computer == "rock"):
        print("Computer wins")
    else:
        print("Its a Tie!!!!!!!!!!")

results = get_choices()
check_win(results.get("player"), results.get("computer"))
