from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
	n = len(gas)

	totalTank = currentTank = 0
	start = 0
	for i in range(n):
		totalTank += gas[i] - cost[i]
		currentTank += gas[i] - cost[i]

		if currentTank < 0:
			start = i + 1
			currentTank = 0

	return start if totalTank >= 0 else -1