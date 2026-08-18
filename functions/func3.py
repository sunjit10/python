import random

seasons = ["summer", "fall", "winter", "spring"]
current_season = random.choice(seasons)
print(current_season)

def get_sport(current_season):
    if (current_season == "fall"):
        sport = "football"
    elif (current_season == "summer"):
        sport = "baseball"
    elif (current_season == "winter"):
        sport = "hockey"
    elif (current_season == "spring"):
        sport = "basketball"
    else:
        sport = "cricket"
    return sport

print(get_sport(current_season))
