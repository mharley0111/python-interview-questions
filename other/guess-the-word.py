from typing import List

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
  def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
    def removeInvalidWord():
      filteredList = []
      for w in wordlist:
        if pairMatches(guessWord, w) == match:
          filteredList.append(w)
                    
      return filteredList
        
    def pairMatches(a, b):
      return sum(c1 == c2 for c1, c2 in zip(a, b))
        
    def getMostCommonWord():
      counts = [[0] * 26 for _ in range(6)]
            
      for w in wordlist:
        for i, c in enumerate(w):
          counts[i][ord(c) - ord('a')] += 1
                    
      bestScore = 0
      bestWord = ""
            
      for w in wordlist:
        currScore = 0
        for i, c in enumerate(w):
          currScore += counts[i][ord(c) - ord('a')]
                    
        if currScore > bestScore:
          bestScore = currScore
          bestWord = w
            
      return bestWord
          
    while wordlist:
      guessWord = getMostCommonWord()
      
      match = master.guess(guessWord)
      
      if match == 6:
        return
      
      wordlist = removeInvalidWord()