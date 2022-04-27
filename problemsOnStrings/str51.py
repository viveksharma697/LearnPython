# Write a Python program to split a string on the last occurrence of the delimiter.

a = "x,y,z,a,s,o,u,r,h,e"
print(a.rsplit(',', 1))
print(a.rsplit(',', 2))
print(a.rsplit(',', 5))