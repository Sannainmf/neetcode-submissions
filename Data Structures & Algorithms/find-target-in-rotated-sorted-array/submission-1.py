class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        minI = l 

        if minI == 0:
            l, r = 0, n - 1
        elif target >= nums[0] and target <= nums[minI - 1]:
            l, r = 0, minI - 1
        else:
            l, r = minI, n - 1

        while l <= r:
            middle = (l + r) // 2
            if nums[middle]  == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1

        return -1


        