from typing import List

"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""
def lengthOfLIS(nums: List[int]) -> int:
	maxSequence = 1
	dp = [1] * len(nums)
	for i in range(len(nums)):
		for j in range(i):
			if nums[i] > nums[j]:
				dp[i] = max(dp[i], dp[j] + 1)
				maxSequence = max(maxSequence, dp[i])
	return maxSequence