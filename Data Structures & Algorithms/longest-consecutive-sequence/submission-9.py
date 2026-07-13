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

        another = []
        longest = 0
        j = 0


        for i in sortArr:
            if not another:
                another.append(i)
            else:
                if i == another[j] + 1:
                    j += 1
                    another.append(i)
                else:
                    longest = max(longest, len(another))
                    another.clear()
                    j = 0
                    another.append(i)

        return max(longest, len(another))




            



            