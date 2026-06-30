class Solution:
    def mySqrt(self, x: int) -> int:

        """
        given non negative integer, return square root of x rounded down to the nearest integer.

        literally just do l = 1, r = x, take the middle, 
        if middle^2 == x, return mid
        if middle^2 > x, l = mid + 1
        if middle^2 < x, r = mid
        """

        l = 1
        r = x

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                r = mid - 1
            elif square < x:
                l = mid + 1

        return l - 1

            


        