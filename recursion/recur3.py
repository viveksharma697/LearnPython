# find the first postion of given character in a string

def find_char(first, pos=0, char='A'):
    if pos<0:
        pos=0
    if pos==len(first):
        return None
    if first[pos] is char:
        return pos
    else:
        return find_char(first, pos+1, char)
    
print("Position of the character is : ", find_char(['1', '2', '3', '4', '5', '6'], 0, '3'))