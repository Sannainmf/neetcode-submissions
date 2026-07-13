class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        stack = []
        for nums, cnt in hash.items():
            stack.append([cnt, nums])

        stack.sort()

        res = []
        while len(res) < k:
            res.append(stack.pop()[1])

        return res