# 2. Sort a list
# Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.

# If the second parameter is "asc," then the function should return a list with the numbers in ascending order. If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.



def sortingLi(li, str):
    y = li
    if str == "none,":
        pass #need some correction here
    
    if str == "asc,":
        li.sort()
        return li

    if str == "desc,":
        li.sort(reverse=True)
        return li


x = [1, 5, 6, 7, 3, 4, 9]
n = "desc,"
print(sortingLi(x, n))
p = "none,"
print(sortingLi(x, p))
o = "asc,"
print(sortingLi(x, o))