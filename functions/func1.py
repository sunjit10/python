def get_choices():
    player_choice = "rock"
    computer_choice = "paper"

    return player_choice


choices = get_choices()
print(choices);print(type(choices))


def get_choices2(computer):
    player_choice = input("Enter the player choice:[rock, paper, scissor] ")
    computer_choice = computer
    choices2 = {"player": player_choice, "computer": computer_choice}
    return choices2

choices_list = get_choices2("paper")
print(choices_list); print(type(choices_list))
