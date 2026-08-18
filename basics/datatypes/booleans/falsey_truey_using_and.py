print("\nTesting for AND")

print("\nIf both are truey, AND prints the second parameter")
print(True and "hello");
print("hello" and True);
print('hi' and 'hey');

print("\nIf both are falsey, AND prints the first parameter")
print([] and False);
print(False and []);

print("\nIf one is truey and one is false, AND prints the falsey value")
print(True and []);
print([] and True);
print(0 and 1);
print(False and "hello");
