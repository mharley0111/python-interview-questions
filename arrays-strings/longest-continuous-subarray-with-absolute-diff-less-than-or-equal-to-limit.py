from typing import List
from collections import deque

def longestSubarray(nums: List[int], limit: int) -> int:
  maxd = deque()
  mind = deque()
  i = 0
  for num in nums:
    while len(maxd) and num > maxd[-1]: maxd.pop()
    while len(mind) and num < mind[-1]: mind.pop()
    maxd.append(num)
    mind.append(num)
    if maxd[0] - mind[0] > limit:
      if maxd[0] == nums[i]: maxd.popleft()
      if mind[0] == nums[i]: mind.popleft()
      i += 1
    
  return len(nums) - i