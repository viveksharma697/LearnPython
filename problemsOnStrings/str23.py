# Write a Python program to sort a string lexicographically.

def sort_lexi(s):
    return sorted(sorted(s), key=str.upper)

print(sort_lexi('quickBrown21'))