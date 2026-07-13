class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        stack = []
        for num, count in hash.items():
            stack.append([count, num])

        stack.sort()

        new = []
        while len(new) < k:
            new.append(stack.pop()[1])
        
        return new