# input returns values a Strings, without it, it might seem it works but it doesn't
# Ex: a = 9, b = 10, it will say 9 is larger is it compares it lexicographically

def compare_nums(num1, num2):
    if (num1 > num2):
      print(num1, "is larger")
    elif (num2 > num1):
      print(num2, "is larger")
    else:
      print("They both are the same")

a = int(input("Enter first number "))
b = int(input("Enter second number "))
compare_nums(a, b)
