"""
LeetCode 1: Two Sum
Idea:
- Use a brute-force approach by checking all possible pairs.
- Return the indices of the two numbers that add up to the target.

Pseudocode:
1. Loop i from 0 to n - 1
2. Loop j from i + 1 to n - 1
3. If nums[i] + nums[j] == target:
      return [i, j]
4. Return empty list if not found
"""

def twoSum(nums, target):
    # Loop through each element
    for i in range(len(nums)):
        # Loop through the next elements
        for j in range(i + 1, len(nums)):
            # Check if the sum equals the target
            if nums[i] + nums[j] == target:
                return [i, j]  # Return indices if found
    return []  # Return empty list if no pair found

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1] because nums[0] + nums[1] == 9

# ---------------------------------------------------

"""
LeetCode 217: Contains Duplicate
Idea:
- Sort the array so that duplicate values are next to each other.
- Check if any two consecutive values are the same.

Pseudocode:
1. Sort the array
2. Loop i from 0 to n - 2
3. If nums[i] == nums[i+1]:
      return True
4. If no duplicates found, return False
"""

def containsDuplicate(nums):
    nums.sort()  # Sort the array
    for i in range(len(nums) - 1):
        # If two consecutive numbers are the same, it's a duplicate
        if nums[i] == nums[i + 1]:
            return True
    return False  # No duplicates found

nums = [1, 2, 3, 4]
print(containsDuplicate(nums))  # Output: False

# ---------------------------------------------------

"""
LeetCode 724: Find Pivot Index
Idea:
- The pivot index is where the sum of the numbers to the left 
  is equal to the sum of the numbers to the right.
- Calculate the total sum of the array.
- Iterate through the array, updating the left sum, and check 
  if left sum == (total sum - left sum - current number).

Pseudocode:
1. totalSum = sum(nums)
2. leftSum = 0
3. Loop i from 0 to n - 1:
      rightSum = totalSum - leftSum - nums[i]
      If leftSum == rightSum:
          return i
      leftSum += nums[i]
4. If no pivot found, return -1
"""

def pivotIndex(nums):
    total_sum = sum(nums)  # Calculate total sum of the array
    left_sum = 0  # Initialize left sum

    for i in range(len(nums)):
        # Calculate right sum by excluding left sum and current element
        right_sum = total_sum - left_sum - nums[i]
        # If left and right sums are equal, return the pivot index
        if left_sum == right_sum:
            return i
        left_sum += nums[i]  # Update left sum

    return -1  # No pivot index found

nums = [1, 7, 3, 6, 5, 6]
print(pivotIndex(nums))  # Output: 3 (pivot index is 3)
