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

        arr.sort()

        newArr = []
        while len(newArr) < k:
            newArr.append(arr.pop()[1])

        return newArr



      


        


        

        

        