from typing import List

def minSwaps(data: List[int]) -> int:
	sizeOfWindow = sum(data)
	zeros = minSwaps = len(data[:sizeOfWindow]) - sum(data[:sizeOfWindow])

	for i in range(sizeOfWindow, len(data)):
		if data[i - sizeOfWindow] == 0:
			zeros -= 1
		if data[i] == 0:
			zeros += 1
		minSwaps = min(minSwaps, zeros)
	
	return minSwaps