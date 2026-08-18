dict1 = {"color": "blue", "age": 30, "isRainy": False}
print(dict1)

print("\npop to fetch and remove")
fav_color = dict1.pop("color")
print(fav_color)
print(dict1) # pop also removes from the dictionary

print("\npopitem retrieves and removes the last item from dictionary")
dict1.popitem()
print(dict1)
