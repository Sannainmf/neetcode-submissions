class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for string in strs:
            sort = tuple(sorted(string))
            if sort not in hashmap:
                hashmap[sort] = [string]
            else:
                hashmap[sort].append(string)

        arr = []

        for value in hashmap.values():
            arr.append(value)

        return arr
        