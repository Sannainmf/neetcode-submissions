class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}

        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        
        stack = []
        for num, cnt in hash.items():
            stack.append([cnt, num])
        
        stack.sort()

        result = []
        while len(result) < k:
            result.append(stack.pop()[1])

        return result

    