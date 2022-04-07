# Write a Python program to find the indexes of numbers of a given list below a given threshold.
# Input:
# [(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
# Output:
# [0, 1, 2, 3, 7, 8, 9, 10]
# Input:
# [(10,(0, 12, 4, 3, 49, 9, 1, 5, 3))]
# Output:
# [0, 2, 3, 5, 6, 7, 8]

def test(nums, n):
    return [i for i,n in enumerate(nums) if n<thresh]

nums=[0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
thresh = 100
print("Original list:")
print(nums)
print("Threshold: ",thresh)
print("Check the indexes of numbers of the said list below the given threshold:")
print(test(nums, thresh))
nums=[0, 12, 4, 3, 49, 9, 1, 5, 3]
thresh = 10
print("\nOriginal list:")
print(nums)
print("Threshold: ",thresh)
print("Check the indexes of numbers of the said list below the given threshold:")
print(test(nums, thresh))