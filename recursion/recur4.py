# counting the number of words in a string


def no_of_words(string, pos=0, count=0, temp=""):
    if pos < 0:
        pos = 0
    if not string:
        return 0
    if pos == len(string) and not temp:
        return count
    elif pos == len(string) and temp:
        print("Found: ", temp)
        temp = ""
        return count+1
    else:
        if string[pos] == " ":
            count += 1
            print("Found: ", temp)
            temp = ""
            return no_of_words(string, pos+1, count, temp)
        else:
            temp += string[pos]
            return no_of_words(string, pos+1, count, temp)


a = "number of words 12 and 13 in this sentence"
print(no_of_words(a), "words")
