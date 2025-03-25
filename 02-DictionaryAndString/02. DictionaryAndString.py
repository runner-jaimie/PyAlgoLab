
## 1. Valid Palindrome (LeetCode #125)

### Problem Description
# Check if the given string `s` is a palindrome considering only alphanumeric characters and ignoring cases.

### Pseudocode
# 1. Initialize an empty string `filtered_s`
# 2. Loop through each character `c` in `s`
#     - If `c` is alphanumeric, append its lowercase version to `filtered_s`
# 3. Use two pointers `left = 0`, `right = len(filtered_s) - 1`
# 4. While `left < right`
#     - If `filtered_s[left] != filtered_s[right]`, return False
#     - Move `left` forward and `right` backward
# 5. Return True

### Python Example Code
def isPalindrome(s):
    filtered = ""
    for c in s:
        if c.isalnum():
            filtered = "".join([filtered, c.lower()])

    left = 0
    right = len(filtered) - 1

    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1

    return True

s = "race a car"
print(isPalindrome(s))  # Output: False


## 2. Reverse String (LeetCode #344)

### Problem Description
# Reverse the input list of characters in-place.

### Pseudocode
# 1. right = len(s) - 1`
# 2. While `left < right`
#     - Swap `s[left]` and `s[right]`
#     - Move `left` forward and `right` backward
# 3. Return the reversed list `s`

### Python Example Code
def reverseString(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

s = ["h", "e", "l", "l", "o"]
print(reverseString(s))  # Output: ['o', 'l', 'l', 'e', 'h']


## 3. Majority Element (LeetCode #169)

### Problem Description
# Find the element that appears more than n/2 times in the array.

### Pseudocode
# 1. Initialize an empty dictionary `my_dict`
# 2. For each element `i` in `nums`
#     - Increment `my_dict[i]` by 1
#     - If `my_dict[i] > n/2`, return `i`
# 3. Return None (though the problem guarantees a majority element)

### Python Example Code
def majorityElement(nums):
    n = len(nums) - 1
    my_dict = {}
    for i in nums:
        my_dict[i] = my_dict.get(i, 0) + 1
        if my_dict[i] > n / 2:
            return i

nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3


## 4. Single Number (LeetCode #136)

### Problem Description
# Find the element that appears only once where every other element appears twice.

### Pseudocode
# 1. Initialize an empty dictionary `count_dict`
# 2. For each number `i` in `nums`
#     - Increment `count_dict[i]` by 1
# 3. Iterate through `count_dict`
#     - If the count of any key is 1, return that key
# 4. Return None

### Python Example Code
def singleNumber(nums):
    count_dict = {}
    for i in nums:
        count_dict[i] = count_dict.get(i, 0) + 1
    for key in count_dict:
        if count_dict[key] == 1:
            return key
    return None

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4
