# Write a Python program to print the following integers with zeros on the left of specified width. 

x = 12
y = 1554
print('Original Number: ', x)
print("Formatted Number: "+"{:0>5d}".format(x))
print("Original Number: ", y)
print("Formatted Number: "+"{:0>7d}".format (y))