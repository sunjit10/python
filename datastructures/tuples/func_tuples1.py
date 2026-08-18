def sayHello(name):
    return name, "Hello " +  name, len(name)

msg = sayHello("Mike")
print(msg)
print(type(msg))
