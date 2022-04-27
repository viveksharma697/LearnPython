# Write a Python function to reverses a string if it's length is a multiple of 4.

def rev_4(str):
    a = len(str)
    b = str[::-1]

    if a % 4 == 0:
        return b
    return str

print(rev_4('font'))
