# Write a Python program to reverse words in a string.


def reverseWords(text):
    for line in text.split('/n'):
        return(' '.join(line.split()[::-1]))
print(reverseWords("This line is written to check whether the words in the line are reversed or not"))
print(reverseWords("Love is greate"))