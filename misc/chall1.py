# Create a Morse Code Translator

# Write a function in python that takes in a string that can have a alphanumeric characters in lower or upper case. The string can also contain any special character handled in Morse code including commas, colons, apostrophes, periods, exclamation marks and question marks. The function should return the morse code equivalent for the string.

dic_mor_code = {'A': '.-', 'B': '-...',
                'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-',
                'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--',
                'X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                '0': '-----', ', ': '--..--', '.': '.-.-.-',
                '?': '..--..', '/': '-..-.', '-': '-....-',
                '(': '-.--.', ')': '-.--.-'}


def codd(line):
    storage1 = ''

    for i in line:
        if i != ' ':
            storage1 += dic_mor_code[i] + ' '

        else:
            storage1 = ' '

    return storage1


def decodd(line):

    line += ' '

    decoded = ''
    encrcode = ''
    for n in line:

        if (n != ' '):
            i = 0
            encrcode += n

        else:
            i += 1

            if i == 2 :
                decoded += ' '
            else:
                decoded += list(dic_mor_code.keys())[list(dic_mor_code.values()).index(encrcode)]
                encrcode = ''
 
    return decoded
 
def check():
    line = "how-are-you"
    result = codd(line.upper())
    print (result)
 
    line = ".... --- .-- -....- .- .-. . -....- -.-- --- ..-"
    result = decodd(line)
    print (result)

check()



