class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        go through each element in array. We start at k = 1, and 
        divide each element in the array by k. The result will
        give us the number we subtract h by. If h is less than 0,
        we increment k, and do the same process for the next, and we 
        return k we go through entirely.
        """

        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            return hours <= h

        l = 1
        r = max(piles)

        while l < r:
            k = (l + r) // 2
            if k_works(k):
                r = k
            else:
                l = k + 1

        return r




            



            
            


            

            

        