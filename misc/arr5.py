# Find a pair with the given sum in an array
# Given an unsorted integer array, find a pair with the given sum in it.

# For example,

# Input:
 
# nums = [8, 7, 2, 5, 3, 1]
# target = 10
 
# Output:
 
# Pair found (8, 2)
# or
# Pair found (7, 3)
 
 
# Input:
 
# nums = [5, 2, 6, 8, 1, 9]
# target = 12
 
# Output: Pair not found


def findPair(nums, target):
 
    
    for i in range(len(nums) - 1):
 
        
        for j in range(i + 1, len(nums)):
 
            
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
    
    print('Pair not found')
 
 

 
nums = [8, 7, 2, 5, 3, 1]
target = 10
 
findPair(nums, target)