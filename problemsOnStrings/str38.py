# Write a Python program to display a number in left, right and center aligned of width 10.

x = 12
print('Original Number: ', x)
print("Right aligned : "+"{:10d}".format(x))
print("Center aligned: "+"{:^10d}".format(x))
print("Left aligned  : "+"{:<10d}".format(x))