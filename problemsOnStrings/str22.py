# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def upperBy4(str):
    numbr = 0
    for letter in str[:4]: 
        if letter.upper() == letter:
            numbr += 1
    if numbr >= 2:
        return str.upper()
    return str

print(upperBy4('Python'))
print(upperBy4('PyThon'))