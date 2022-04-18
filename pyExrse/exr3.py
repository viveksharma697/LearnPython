# 4. Count the vowels in a string
# Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, and u will be counted as vowels — not y.

def countVowels(str):
    count = 0
    x = set("aeiouAEIOU")
    for i in str:
        if i in x:
            count += 1            
    return count

y = "elephant"
print(countVowels(y))