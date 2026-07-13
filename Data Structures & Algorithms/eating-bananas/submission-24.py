class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        """
        given array piles

        piles[i] is the unmber of bananas in ith pile

        you can choose bananas per houreating rate of k (binary search this)

        each hour, you can chosoe a pile of baannas and eat k bananas form that pile

        if that pile has less than k banans, you may finihs eating the pile,
        but you cannot eat from another pile in the same hour

        return minimum integer k such that you can eat all
        the bananas within h hours
        """ 

        l = 1
        r = max(piles)

        while l < r:
            rate = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += pile // rate

                if pile % rate != 0:
                    hours += 1

            if hours > h:
                l = rate + 1
            else:
                r = rate

        return l


        