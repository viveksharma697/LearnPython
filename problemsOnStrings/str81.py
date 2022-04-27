# Write a Python program to find the index of a given string at which a given substring starts. If the substring is not found in the given string return 'Not found'.

def find_Index(str1, y):
  if str1.find(y) in range(len(str1)):
    return str1.find(y)
  else:
    return "not found"

print(find_Index("Python Exercises", "Ex"))
print(find_Index("Python Exercises", "yt"))
print(find_Index("Python Exercises", "Pt"))