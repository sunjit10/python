# Similar to rock_paper_scissors.py except for refactored if statement
# refactored if statement shows a nested if statement
import random

pick_one = ["rock", "paper", "scissors"]

def get_choices():
    player_choice = input("Enter your choice ")
    computer_choice = random.choice(pick_one)
    return {"player": player_choice, "computer": computer_choice}

def check_win2(player, computer):
    print(f"You chose {player}, and computer chose {computer}")
    if (player == computer):
        print("Its a Tie!!!!!!!!!!")

    if (player == "rock"):
        if (computer == "paper"):
            print("Computer wins")
        elif (computer == "scissors"):
            print("You Win!!!")
    elif (player == "paper"):
        if (computer == "scissors"):
            print("Computer wins")
        elif (computer == "rock"):
            print("You Win!!!")
    elif (player == "scissors"):
        if (computer == "rock"):
          print("Computer wins")
        if (computer == "paper"):
          print("You win")


results = get_choices()
check_win2(results["player"], results["computer"])
