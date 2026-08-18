# Function must have a colon at the end and start with def
# Function body is based on indentation
def get_weather():
    return "Spring"

current_weather = get_weather()
print(current_weather); print(get_weather())


# It is not get_temp(<variable_type> variable)
def get_temp(weather):
    if (weather == "Spring"):
        return "mild"

print(get_temp("Spring"))

# Guess what will happen for line below
print(get_temp("Summer")); print(type(get_temp("Summer")))

