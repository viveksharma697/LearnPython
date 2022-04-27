# Write a Python program to count the occurrences of each word in a given sentence.

def wordCount(a):
    b = dict()
    c = a.split()

    for word in c:
        if word in b:
            b[word] += 1
        else:
            b[word] = 1

    return b

print(wordCount('twinkle twinkle little star'))

