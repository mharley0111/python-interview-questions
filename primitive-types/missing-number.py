from typing import List

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def missingNumber(nums: List[int]) -> int:
	missing = len(nums)
	for i, num in enumerate(nums):
		missing ^= i ^ num

	return missing


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def missingNumber2(nums: List[int]) -> int:
	numSet = set(nums)
	n = len(nums) + 1
	for number in range(n):
		if number not in numSet:
			return number