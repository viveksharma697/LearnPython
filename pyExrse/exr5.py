# Repeat the characters
# Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".

def double(str):
    a = ""
    for i in str:
        a += i * 2
    return a

strr = "love"
print(double(strr))
