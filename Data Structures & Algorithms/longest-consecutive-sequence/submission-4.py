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

        sortArr = sorted(arr)
        j = 0
        another = []
        longest = 0

        for i in sortArr:
            if not another:
                another.append(i)
            else:
                if i == another[j] + 1:
                    another.append(i)
                    j += 1
                else:
                    longest = max(longest, len(another))
                    another.clear()
                    another.append(i)
                    j = 0

        return max(longest, len(another))


                   



            