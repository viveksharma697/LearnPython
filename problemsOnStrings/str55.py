# Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest

def first_repeated_char_smallest_distance(str1):
  temp = {}
  for n in str1:
    if n in temp:
      return n, str1.index(n);
    else:
      temp[n] = 0
  return 'None'
print(first_repeated_char_smallest_distance("abcabc"))
print(first_repeated_char_smallest_distance("abcb"))
print(first_repeated_char_smallest_distance("abcc"))