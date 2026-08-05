class Solution:


    def findErrorNums(self, nums: List[int]) -> List[int]:

        hsh = {}
        res = []

        for num in nums:
            if num not in hsh:
                hsh[num] = 1
            else:
                res.append(num)

        for i in range(1, len(nums) + 1):
            if i not in hsh:
                res.append(i)
                return res





        
        
        