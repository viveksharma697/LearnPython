# Write a Python program to count and display the vowels of a given text.

def vowel(text):
    vowels = "aeiouAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])

vowel('Lets check how many vowels are present here')