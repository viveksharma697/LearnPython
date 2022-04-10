# find the difference between the two strings, the function should return the extra character. For example, if the first parameter is "eueiieo" and the second is "iieoedue" then the function should return 'd'

def uncommon_chars(s1, s2):   
     
  
     extra_char = list(s1 or s2) 
     result = [ch for ch in s1 if ch not in extra_char] + [ch for ch in s2 if ch not in extra_char] 
     return(''.join(result))

s1 = 'eueiieo'
s2 = 'iieoedue'
print("Original Substrings:\n",s1+"\n",s2)
print("\nThe extra character is:")
print(uncommon_chars(s1, s2))