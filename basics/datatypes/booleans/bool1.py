# Boolean values: True or False
# Boolean Operators: and or not
import random

c1 = random.choice([True, False]);
c2 = random.choice([True, False]);

print(type(c1) == bool and type(c2) == bool);
print(f"c1 is {c1} and c2 is {c2}")

if (c1 and c2):
    print("Both are True");

if (c1 or c2):
    print("One of them is True");

if (not c1):
    print("c1 is False");

if (not c2):
    print("c2 is False");

