class Solution:
    def minWindow(self, s: str, t: str) -> str:

        smallString = s + "X"
        countT = {}
        countZ = {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        for l in range(len(s)):
            countZ = {}
            for r in range(l + 1, len(s) + 1):
                char = s[r - 1]

                if char in countT:
                    countZ[char] = countZ.get(char, 0) + 1

                valid = True
                for char, count in countT.items():
                    if countZ.get(char, 0) < count:
                        valid = False
                        break

                if valid and len(s[l : r]) < len(smallString):
                    smallString = s[l : r]

        return smallString if len(smallString) <= len(s) else ""
        


                    




                


                    


        