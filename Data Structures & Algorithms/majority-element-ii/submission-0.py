class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hsh = {}

        for num in nums:
            if num not in hsh:
                hsh[num] = 1
            else:
                hsh[num] += 1

        arr = []

        for num in hsh.keys():
            count = hsh[num]
            if count > len(nums) / 3:
                arr.append(num)

        return arr


        


        