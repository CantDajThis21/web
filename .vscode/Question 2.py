def str_rep(x, z):
    if z > 0:
        txt = ''
        for i in range(z):
            txt += x
        return txt
    else:
        print("Invalid Number!")


print(str_rep("Dodge", 5))
print(str_rep("Dodge", 3))
print(str_rep("Dodge", 1))