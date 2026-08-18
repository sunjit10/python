# Tuples are immutable
# Cannot Add/Remove from it
names = ("Mike", "Adam", "James", "Bob", "Greg")
print(names);

print(names[1])
print(names[-1])
print(names.index("Adam"))

print(len(names))


print("James" in names)
print(names[2:4])

print("\nsorting tuples")
print(sorted(names))
# Unlike list, the tuple does not change
print(names)

print("\ncreating new tuples from original")
names2 = names + ("Jim", "Chris")
print(names2)
print(names)
