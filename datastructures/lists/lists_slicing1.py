# list[a:b] = [...]
# If a < b → replace elements
# If a >= b → insert at position a
mylist1 = [10,20,30,40,50]

# [start_inclusive_index:end_exclusive_index]
mylist1[3:1] = [35]
print(mylist1)

mylist1[2:6] = ["A", "B", "C", "D"]
print(mylist1)
