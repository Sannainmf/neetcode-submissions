from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        sortT = ''.join(sorted(t))
        sortS = ''.join(sorted(s))

        if sortS == sortT:
            return True
        else:
            return False




        
        