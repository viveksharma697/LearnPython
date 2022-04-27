# Write a Python code to remove all characters except a specified character in a given string.
# Original string
# Python Exercises
# Remove all characters except P in the said string:
# P
# Original string
# google
# Remove all characters except g in the said string:
# gg
# Original string
# exercises
# Remove all characters except e in the said string:
# eee


def remove_characters(str1, c):
    return ''.join([al for al in str1 if al == c])


text = "Python Exercises"
print("Original string")
print(text)
except_char = "P"
print("Remove all characters except", except_char, "in the said string:")
print(remove_characters(text, except_char))
text = "google"
print("\nOriginal string")
print(text)
except_char = "g"
print("Remove all characters except", except_char, "in the said string:")
print(remove_characters(text, except_char))
text = "exercises"
print("\nOriginal string")
print(text)
except_char = "e"
print("Remove all characters except", except_char, "in the said string:")
print(remove_characters(text, except_char))
