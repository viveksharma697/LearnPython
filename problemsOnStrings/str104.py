# total sum with the help of the lambda function

from functools import reduce

a = [1,2,3,4,5,6,7,8,9,10]
n = reduce(lambda x,y:x+y, a)
print(n)