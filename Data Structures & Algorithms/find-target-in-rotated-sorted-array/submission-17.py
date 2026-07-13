class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle

        minIndex = l

        if minIndex == 0:
            l = 0
            r = len(nums) - 1
        elif target >= nums[0] and target <= nums[minIndex - 1]:
            l = 0
            r = minIndex - 1
        else:
            l = minIndex
            r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1

        return l if nums[l] == target else -1
        

        
        

        