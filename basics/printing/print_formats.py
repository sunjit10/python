age = 20
weight = 189.34
gender = "male"

###### Scenario 1: Old school printing like in Java
# print("You are " + age + " years old");

# !!! The above won't work in python since only strings can be concatenated

# Need to explicitly cast it to String using str(age)
print("You are " + str(age) + " years old");
# Can use gender as is since its a String
print("Your are a " + gender);



###### Scenario 2: Comma separated
print("You are", age, "years old and weigh", weight, "pounds")
# Will the output be: You are 20 or You are20?  Its the former.




##### Scenario 3: Using f strings
# Use f strings that allows you to use curly braces
print(f"You are {20} years old and weigh {weight} pounds")
# Advantage? You cn use expressions within {}





##### Scenario 4: Using 3 double quotes
# Using 3 quotes allow you preserve the format
print(f"""You


are


{age}


years


old!
""")

