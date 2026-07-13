class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l < r:
            middle = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += pile // middle
                if pile % middle != 0:
                    hours += 1
                
            if hours <= h:
                r = middle
            else:
                l = middle + 1

        return l
        