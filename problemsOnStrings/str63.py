# Write a Python program to remove leading zeros from an IP address.

def withoutZero(ip_add):
  new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])  
  return new_ip_add 

print(withoutZero("255.024.01.01"))
print(withoutZero("127.0.0.01 "))
