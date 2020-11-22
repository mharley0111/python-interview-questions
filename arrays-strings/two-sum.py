from typing import List
from collections import defaultdict

def twoSum(nums: List[int], target: int) -> List[int]:
	seen = defaultdict(int)
	for i in range(len(nums)):
		compliment = target - nums[i]
		if compliment in seen:
			return [seen[compliment], i]
		seen[nums[i]] = i

	return []