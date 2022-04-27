# Write a Python program to split a given multiline string into a list of lines.
# Sample Output:
# Original string: This
# is a
# multiline
# string.
# Split the said multiline string into a list of lines:
# ['This', 'is a', 'multiline', 'string.', '']

def split_lines(s):
  return s.split('\n')
print("Original string:")
print("This\nis a\nmultiline\nstring.\n")
print("Split the said multiline string into a list of lines:")
print(split_lines('This\nis a\nmultiline\nstring.\n'))