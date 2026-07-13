class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        arr = []

        for i in nums:
            if not arr:
                arr.append(i)
            else:
                if i in arr:
                    continue
                else:
                    arr.append(i)


        arr.sort()
        new = []
        longest = 0
        j = 0

        for i in arr:
            if not new:
                new.append(i)
            else:
                if i == new[j] + 1:
                    new.append(i)
                    j += 1
                else:
                    longest = max(longest, len(new))
                    new.clear()
                    new.append(i)
                    j = 0
                    

        return max(longest, len(new))

