class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hsh = {}

        for num in nums:
            if num in hsh:
                hsh[num] += 1
            else:
                hsh[num] = 1

        for i, f in hsh.items():
            if f > len(nums) // 2:
                return i

        