mylist1 = ["Jim", 23, 22.111, False, "James"]
print("\nChange items in list")
mylist1[2] = "Yooo"
print(mylist1)

print("\nAppend to list")
mylist1.append(50) # append can add only 1 value
print(mylist1)

mylist1.insert(2, "Robert")
print(mylist1)

# extend allows you to add multiple values
mylist1.extend(["A", "B", "C"])

print(mylist1)

mylist1 += ["Cow", "Dog"]
print(mylist1)

# Without square brackets, each letter gets added individually
mylist1 += "Cat"
print(mylist1)
