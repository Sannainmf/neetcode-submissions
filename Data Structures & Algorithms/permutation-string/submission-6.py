class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        r = len(s1)

        sort_s1 = sorted(s1)

        while r <= len(s2):
            if sort_s1 == sorted(s2[l : r]):
                return True

            l += 1
            r += 1

        return False