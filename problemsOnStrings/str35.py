# Write a Python program to print the following integers with '*' on the right of specified width.

x = 12
y = 1554
print('Original Number: ', x)
print("Formatted Number: "+"{:*<5d}".format(x))
print("Original Number: ", y)
print("Formatted Number: "+"{:*<7d}".format (y))