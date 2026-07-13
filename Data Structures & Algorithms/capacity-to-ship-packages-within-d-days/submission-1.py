class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)
        cap = ('-inf')

        while l <= r:
            mid = (l + r) // 2
            total = 0
            index = 0
            for weight in weights:
                total += weight
                
                if total > mid:
                    index += 1
                    total = weight
            
            index += 1

            if index > days:
                l = mid + 1
            else:
                r = mid - 1

        return l
            





                
        