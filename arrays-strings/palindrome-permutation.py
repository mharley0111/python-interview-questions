# Time Complexity: O(n)
# Space Complexity: O(n)

def canPermutePalindrome(s: str) -> bool:
	table = buildCharFrequencyTable(s)
	return checkMaxOneOdd(table)

def chackMaxOneOdd(table: dict) -> bool:
	foundOdd = False
	for count in table.values():
		if count % 2 == 1:
			if foundOdd:
				return False
			foundOdd = True
	return True

def buildCharFrequencyTable(s: str) -> dict:
	table = {char: 0 for char in s}
	for char in s:
		table[char] += 1
	return table