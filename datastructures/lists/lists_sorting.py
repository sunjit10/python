ages = [30, 10, 50, 45, 70, 55, 25]
ages.sort()
print(ages)

age = [30, 35, 20, 15, 45, 40]
age_original = age[:]
age.sort()
print(age)
print(age_original)

# Sort does Upper case first followed by Lower case
fnames = ["mike", "john", "zack", "Sam", "John", "bob"]
fnames.sort()
print(fnames)

# You can force to sort 
fnames = ["mike", "john", "zack", "tim", "Sam", "John", "bob"]
fnames.sort(key=str.lower)
print(fnames)
