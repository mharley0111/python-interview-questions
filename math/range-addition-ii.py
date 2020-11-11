from typing import List

def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
	if len(ops) == 0: return m * n
	if (m * n) == 1: return 1

	minX = float("inf")
	minY = float("inf")
	for op in ops:
		minX = min(minX, op[0])
		minY = min(minY, op[1])
	
	return minX * minY