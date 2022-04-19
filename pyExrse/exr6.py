#  Are the Xs equal to the Os?
# Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. It should then return a boolean value of either True or False.

# If the count of Xs and Os are equal, then the function should return True. If the count isn't the same, it should return False. If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string can contain any type and number of characters.


def check(str):
    a = 0
    b = 0
    for i in str:
        if i == "o" or i == "O":
            a += 1
    for j in str:
        if j == "x" or j == "X":
            b += 1
    if a == b:
        return True
    else:
        return False


n = "this is xax open"
print(check(n))
