# Check if a subarray with 0 sum exists or not
# Given an integer array, check if it contains a subarray having zero-sum.

# For example,

# Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

# Output: Subarray with zero-sum exists

# The subarrays with a sum of 0 are:

# { 3, 4, -7 }
# { 4, -7, 3 }
# { -7, 3, 1, 3 }
# { 3, 1, -4 }
# { 3, 1, 3, 1, -4, -2, -2 }
# { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }


def hasZeroSumSublist(nums):

    s = set()

    s.add(0)

    total = 0

    for i in nums:

        total += i

        if total in s:
            return True

        s.add(total)

    return False


nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

if hasZeroSumSublist(nums):
    print('Subarray with zero-sum exists')
else:
    print('Sublist does not exist')
