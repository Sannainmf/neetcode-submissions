class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}

        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] = hash[num] + 1

        arr = []
        another = []

        for num, cnt in hash.items():
            arr.append([cnt, num])

        sortArr = sorted(arr)

        while len(another) < k:
            another.append(sortArr.pop()[1])

        return another
        
