class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        newArr = []

        for i in nums:
            if not newArr:
                newArr.append(i)
            else:
                if i in newArr:
                    continue
                else:
                    newArr.append(i)

        thing = sorted(newArr)
        arr = []
        longest = 0


        for i in range(len(thing)):
            if not arr:
                arr.append(thing[i])
            else:
                if arr[len(arr) - 1] + 1 == thing[i]:
                    arr.append(thing[i])
                    longest = max(longest, len(arr))
                else:
                    arr.clear()
                    arr.append(thing[i])

        return max(longest, len(arr)) 