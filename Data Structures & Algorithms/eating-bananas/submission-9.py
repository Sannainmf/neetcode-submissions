class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #Its important to understand that for every binary search problem,
        #you need a lower and upper limit\
        """
        Here's what we'll do. lower limit will be 1 b/hr, because this is the lowest rate 
        koko can eat bananas. The highest banana eating rate will be the max of the piles list.
        Binary search with these two bounds, we calculate the middle eating banana rate - see how long
        it takes for koko to eat all the bananas. If the num of hrs is more than h, we need a higher
        eating rate, which is done by making left mid + 1. If its less than h we need a slower eating rate, 
        which we do making right mid
        """

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
        
