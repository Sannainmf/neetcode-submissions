class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        s = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    arr = [nums[i], nums[j], nums[k]]
                    arr.sort()
                    if arr[0] + arr[1] + arr[2] == 0:
                        s.add(tuple(arr))

        return [list(t) for t in s]



                        