from typing import List

"""
New Version
"""
def threeSumSmaller(nums: List[int], target: int) -> int:
	nums.sort()
	total = 0
	for i in range(len(nums) - 2):
		total += twoSumSmaller(nums, i + 1, target - nums[i])
	
	return total


def twoSumSmaller(nums: List[int], startIndex: int, target: int) -> int:
	total = 0
	left = startIndex
	right = len(nums) - 1
	while left < right:
		if nums[left] + nums[right] < target:
			total += right - left
			left += 1
		else:
			right -= 1
	
	return total

"""
Old Version
"""
# def threeSumSmaller(nums: List[int], target: int) -> int:
# 	nums.sort()
# 	count = 0
# 	for k in range(len(nums)):
# 		i, j = 0, k - 1
# 		while i < j:
# 			if nums[i] + nums[j] + nums[k] < target:
# 				count += j - i
# 				i += 1
# 			else:
# 				j -= 1
# 	return count
