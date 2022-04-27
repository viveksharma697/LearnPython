# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9




def longestWord(w_list):
    w_len = []
    for n in w_list:
        
        w_len.append((len(n), n))
    w_len.sort()
    return w_len[-1][0], w_len[-1][1]

result = longestWord(["Basic", "Exercises", "Fontsize"])
print("Longest word: ",result[1])
print("Length of the longest word: ",result[0])