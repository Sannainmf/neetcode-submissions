class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0
        j = 1

        for num in nums:
            if (num - 1) not in s:
                nextNum = num + 1
                length = 1
                while nextNum in s:
                    length += 1
                    nextNum += 1
                
                longest = max(longest, length)

        return longest
            
                


