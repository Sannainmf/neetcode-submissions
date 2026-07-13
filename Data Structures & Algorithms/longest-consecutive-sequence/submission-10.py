class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        arr = []

        for i in nums:
            if not nums:
                arr.append(i)
            else:
                if i in arr:
                    continue
                else:
                    arr.append(i)

        another = []
        sort = sorted(arr)
        longest = 0
        j = 0

        for i in sort:
            if not another:
                another.append(i)
            else:
                if i == another[j] + 1:
                    another.append(i)
                    j += 1
                else:
                    longest = max(longest, len(another))
                    j = 0
                    another.clear()
                    another.append(i)

        return max(longest, len(another))



