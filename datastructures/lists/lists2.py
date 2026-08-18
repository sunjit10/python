# Can have duplicates
# Can have different data types mixed together
mylist1 = ["Mike", 1, True, "Hello", 34.33, True, 1]

print("\nPrint items in the list")
print(mylist1[3])
print(mylist1[-3])
print(mylist1[2:4])
print(mylist1[:3])
print(mylist1[4:])

print("\nCheck for items in a list")
print(34.33 in mylist1);
print("Michael" in mylist1);


print("\nEmpty List")
mylist2 = []
print(len(mylist2))
# print(mylist2[0])  Will throw index out of range error


