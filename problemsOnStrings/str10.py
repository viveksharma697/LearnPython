# Write a Python program to remove the nth index character from a nonempty string.

def remove_n(str, n):
    x = str[:n]
    y = str[n+1:]
    return x + y
print(remove_n('love', 2))
print(remove_n('love', 1))
print(remove_n('love', 3))

    