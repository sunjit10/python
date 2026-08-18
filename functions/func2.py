def get_sport(season):
    if (season == "fall"):
        return "football"
    else:
        return "cricket"

def get_season():
    return "summer"

sport = get_sport(get_season())
print(sport)
