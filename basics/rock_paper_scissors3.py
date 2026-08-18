import random

pick_one = ["rock", "paper", "scissors"]

def get_choices():
    player_choice = input("Enter your choice ")
    computer_choice = random.choice(pick_one)
    return {"player": player_choice, "computer": computer_choice}


def check_win3(player, computer):
    print(f"You chose {player}, and computer chose {computer}")
    
    if player == computer:
        print("It's a Tie!!!!!!!!!!")
    elif (player, computer) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
        print("You Win!!!")
    else:
        print("Computer wins")

results = get_choices()
check_win3(results.get("player"), results.get("computer"))
