class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        r = len(s1)

        s1_sort = sorted(s1)

        while r <= len(s2):
            if s1_sort == sorted(s2[l : r]):
                return True

            l += 1
            r += 1

        return False        