def value(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    else:
        return False


print(value(3))
print(value(3.7))
print(value(""))
