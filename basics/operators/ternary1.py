age = 19

def check_can_vote():
    if age < 21:
        return False;
    else:
        return True;

# Python Ternary operator
def check_can_vote2():
    return True if age > 21 else False;

print(check_can_vote2())

