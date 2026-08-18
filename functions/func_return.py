# Empty return statement
# As soon as return statement is encountered, function returns
def sayHello(name):
    if not name:
        print("Empty return")
        return
    return "Hello " +  name

msg = sayHello("Mike")
print(msg);

# sayHello() won't run, had to use sayHello(False)
sayHello(False)
