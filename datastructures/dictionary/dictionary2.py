dict1 = {"color": "blue", "age": 30, "isRainy": False}
print(dict1)

dict1["isRainy"] = True
dict1["color"] = "yellow"

print(dict1)
 
# If there is temp, it returns its value. Else uses the value provided. It does not modify the dictionary
print(dict1.get("temp", "warm"))
print(dict1)

# Add an element to dictionary at the end
dict1["shape"] = "square"
print(dict1)

# Remove an element
del dict1["age"]
print(dict1)

