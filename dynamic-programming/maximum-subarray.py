from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def maxSubArray(nums: List[int]) -> int:
	maxSum = nums[0]
	for i in range(1, len(nums)):
		if nums[i - 1] > 0:
			nums[i] += nums[i - 1]
		maxSum = max(nums[i], maxSum)
	
	return maxSum