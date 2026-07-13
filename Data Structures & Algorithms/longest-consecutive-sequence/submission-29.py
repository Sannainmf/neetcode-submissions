class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        newArr = sorted(nums)
        arr = []

        for i in newArr:
            if not arr:
                arr.append(i)
            elif i in arr:
                continue
            else:
                arr.append(i)

        longest = 0

        l = 0 
        r = 1
        temp = 0

        if len(arr) == 1:
            return 1

        while r < len(arr):
            if arr[l] + 1 == arr[r]:
                longest = max(longest, r - temp + 1)
                l += 1
                r += 1
            else:
                l = r
                r += 1
                temp = l

        return longest