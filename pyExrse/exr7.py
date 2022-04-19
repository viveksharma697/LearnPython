#  Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "4444444444444444", then it should return "4444".

def hideNo(str):
    
    store = ""

    for i in range(11):

        if len(str) == 16:
            store += "*"
        
        else:
            print("Please enter a valid number")
    print(store + str[12:16])

n = "12546547156492"

print(hideNo(n))