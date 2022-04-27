# Write a Python program to strip a set of characters from a string.

def strip(str, str1):
    return "".join(c for c in str if c not in str1)

print("Original String: ")
print("This line is just check the stripped characters")
print("After stripping a,e,i,o,u")      
print(strip("This line is just check the stripped characters", "aeiou"))