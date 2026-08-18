print("\nTesting for OR")


print("\nIf one is truey and one is false, OR prints the truey value")
print(0 or 1);
print(1 or 0);
print(False or "hello");
print(True or []);
print([] or True);

print("\nIf both are truey, OR prints the first parameter")
print(True or "hello");
print('hi' or 'hey');

print("\nIf both are falsey, OR prints the first parameter")
print([] or False);
print(False or []);
