class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        arr = []

        for key, value in hashmap.items():
            arr.append([value, key])

        arr.sort()

        newArr = []


        while len(newArr) < k:
            newArr.append(arr.pop()[1])

        return newArr


        

        
        