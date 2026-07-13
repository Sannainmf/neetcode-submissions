class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        # [-4, -1, -1, 0, 1, 2]
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = len(nums) - 1
            
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1 
                elif s > 0:
                    high -= 1
                else:
                    low += 1

        return res
