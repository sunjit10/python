from enum import Enum

# Enum is the only way to define Constants (immutable values)
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE)
print(type(State.ACTIVE))
print(isinstance(State.ACTIVE, State))

print("\nGet the value of Enum")
print(State.ACTIVE.value)
print(State(1))
print(type(State.ACTIVE.value))

print("\nUsing square brackets");
print(State['ACTIVE'])
print(State['ACTIVE'].value)

print("\nShow all elements and its size")
print(list(State))
print(len(State))
