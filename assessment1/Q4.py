# Q4. Customer Ratings Analysis
# Given an array of ratings:
# a) Find all peak elements.
# b) Find majority element or sort by frequency.
# c) Find maximum subarray sum.

from collections import Counter
arr = [1, -3, 2, -4, 1, 5, -3, 6, -4, 5, 7, 6]
print("Peak elements:", [arr[i] for i in range(1, len(arr)-1) if arr[i] > arr[i-1] and arr[i] > arr[i+1]])
freq = Counter(arr)
def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
print("Maximum subarray sum:", max_subarray_sum(arr))
