class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        arr = []
        diff = []


        for i in nums:
            if not arr:
                arr.append(i)
            else:
                if i in arr:
                    continue
                else:
                    arr.append(i)


        sortNums = sorted(arr)

        j = 0
        longest = 0

        for i in sortNums:
            
            if not diff:
                diff.append(i)
            else:
                if i == diff[j] + 1:
                    diff.append(i)
                    j += 1
                else:
                    longest = max(longest, len(diff))
                    diff.clear()
                    diff.append(i)
                    j = 0

        return max(longest, len(diff))

        