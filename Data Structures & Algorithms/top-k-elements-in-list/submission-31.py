class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        arr = []
        
        for i, j in hash.items():
            arr.append([j, i])

        newArr = sorted(arr)
        another = []
        while len(another) < k:
            another.append(newArr.pop()[1])

        return another


