# Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list.
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input:
# [19, 15, 5, 7, 5, 5, 2]
# Output:
# False
# Input:
# [11, 12, 14, 13, 14, 13, 15, 14]
# Output:
# True
# Input:
# [19, 15, 11, 7, 5, 6, 2]
# Output:
# False

def test(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3

nums = [19,19,15,5,5,5,1,2]
print("Original list:")
print(nums)
print("Check whether the length of the said list is 8 and fifth element occurs thrice in the said list. :")
print(test(nums))
nums = [19,15,5,7,5,5,2]
print("\nOriginal list:")
print(nums)
print("Check whether the length of the said list is 8 and fifth element occurs thrice in the said list. :")
print(test(nums))
nums = [11,12,14,13,14,13,15,14]
print("\nOriginal list:")
print(nums)
print("Check whether the length of the said list is 8 and fifth element occurs thrice in the said list. :")
print(test(nums))
nums = [19,15,11,7,5,6,2]
print("\nOriginal list:")
print(nums)
print("Check whether the length of the said list is 8 and fifth element occurs thrice in the said list. :")
print(test(nums))