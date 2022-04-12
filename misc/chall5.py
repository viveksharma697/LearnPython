# convert a binary number to the hexadecimal number

table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
                    13: 'd', 14: 'e', 15: 'f'}
  
def deciToHex(numd):
    hexadecimal = ''
    while(numd > 0):
        remainder = numd % 16
        hexadecimal = table[remainder] + hexadecimal
        numd = numd / 16
  
    return hexadecimal
  
  
n = int(input("Enter the binary number : "))
print("The hexadecimal form of", n,
      "is", deciToHex(n))