class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        stack = []
        for num, cnt in hash.items():
            stack.append([cnt, num])

        stack.sort()

        result = []

        while len(result) < k:
            result.append(stack.pop()[1])

        return result