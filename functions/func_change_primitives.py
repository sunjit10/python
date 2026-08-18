def change(val):
    val += 10
    print("val inside func", val)
    return val

val = 3

change(val)
print("val outside func", val)
