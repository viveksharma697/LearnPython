# Write a Python program to find list integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.
# Input:
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Output:
# True
# Input:
# [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# Output:
# False
# Input:
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# Output:
# False

def test(nums):
    return all([nums[i] != nums[i + 1] for i in range(len(nums)-1)]) and len(set(nums)) == 4
nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print("Original list:")
print(nums)
print("Check said list of integers containing exactly four distinct values, such that no integer repeats  twice consecutively:")
print(test(nums))
nums = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
print("\nOriginal list:")
print(nums)
print("Check said list of integers containing exactly four distinct values, such that no integer repeats  twice consecutively:")
print(test(nums))
nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print("\nOriginal list:")
print(nums)
print("Check said list of integers containing exactly four distinct values, such that no integer repeats  twice consecutively:")
print(test(nums))