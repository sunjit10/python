# Python uses and vs &&
# input function is type string, need to cast it to int
# else if -> elif
# every if, elif, else ends with :

def compare_nums_v2(num1, num2):
    if (num1 > 0 and num1 > num2):
      print(num1, "is larger")
    elif (num2 > 0 and  num2 > num1):
      print(num2, "is larger")
    else:
      print("They both are the same")

a = int(input("Enter first number "))
b = int(input("Enter second number "))
compare_nums_v2(a, b)
