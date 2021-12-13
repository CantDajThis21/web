def monkey_trouble(a_smile, b_smile):
    if a_smile is True and b_smile is True:
        return True
    elif a_smile is True and b_smile is False:
        return False
    elif a_smile is False and b_smile is False:
        return True
    elif a_smile is False and b_smile is True:
        return False


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))

