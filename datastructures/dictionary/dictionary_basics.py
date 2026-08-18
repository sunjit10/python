sky_color = "blue"
dict1 = {"name": "beau", "color": sky_color}

# You can mix single and double, as long as you open and end with the same
dict2 = {"season": 'spring', "temp": 'mild'}
print(dict2)
print(len(dict2))

# Two different ways of getting values from dictionary
# dictionary["key"]
# dictionary.get("key")
season_is = dict2["season"]
temp_is = dict2.get("temp")

print(f"It is {temp_is} in {season_is}")

print("season" in dict1); # returns False
print("season" in dict2); # returns True
