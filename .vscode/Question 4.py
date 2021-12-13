def reverse_list(z):
    x = list(set(z))
    print("Array is:", x)
    print("Reversed Array is:", list(reversed(x)))


print(reverse_list(z=[1, 2, 3, 4, 5, 5, 6]))
print(reverse_list(z=[5, 1, 2, 3, 7]))
print(reverse_list(z=[1, 2, 1, 10, 7, 51, 5, 53, 3]))
