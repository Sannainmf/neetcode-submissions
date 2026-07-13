class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT = {}
        countZ = {}
        
        smallString = s + "X"

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        for l in range(len(s)):
            countZ = {}
            for r in range(l + 1, len(s) + 1):
                char = s[r - 1]

                if char in countT:
                    countZ[char] = countZ.get(char, 0) + 1

                condition = True
                for char, count in countT.items():
                    if countZ.get(char, 0) < count:
                        condition = False
                        break
                
                if condition and len(s[l : r]) < len(smallString):
                    smallString = s[l : r]

        return smallString if len(smallString) <= len(s) else ""


        