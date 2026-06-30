class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        """
        conveyor belt has packages that must be shipped from one
        port to another within x days.

        the ith weight on the package jas a weight of weights[i]
        it is not allowed to load weight more than the maximum weight capacity
        of the ship

        return least weight cap of the ship that will result in all the packages
        on the conveyor belt being shipped within x days
        """

        """
        essentially we will be setting l to 1, r to max(weight).
        Get the middle, for loop in the while loop, if
        an element greater than middle
        """

        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l + r) // 2
            
            res = 0
            counter = 1
            for w in weights:
                res += w
                if res > mid:
                    counter += 1
                    res = w

            if counter > days:
                l = mid + 1
            else:
                r = mid - 1

        return l
        
                

                

        
