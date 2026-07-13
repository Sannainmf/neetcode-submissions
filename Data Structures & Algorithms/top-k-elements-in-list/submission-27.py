class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}

        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        arr = []
        for num, cnt in hash.items():
            arr.append([cnt, num])

        sortArr = sorted(arr)

        another = []

        while len(another) < k:
            another.append(sortArr.pop()[1])

        return another