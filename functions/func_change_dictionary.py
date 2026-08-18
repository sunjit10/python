def change(val):
    val["color"] = "yellow"
    print("val inside func", val)
    return val

val = {"color":"blue"}
print("We started with this", val)

change(val)
print("val outside func", val)
