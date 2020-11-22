from typing import List

def fizzBuzz(n: int) -> List[str]:
	ans = []

	fizzBuzzDict = {3: "Fizz", 5: "Buzz"}
	fizzBuzzKeys = sorted(list(fizzBuzzDict.keys()))

	for i in range(1, n + 1):
		currentStr = ""

		for key in fizzBuzzKeys:
			if i % key == 0:
				currentStr += fizzBuzzDict[key]

		if not currentStr:
			currentStr = str(i)

		ans.append(currentStr)

	return ans