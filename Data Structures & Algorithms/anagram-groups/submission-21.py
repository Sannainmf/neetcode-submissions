class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hsh = {}
        arr = []

        for string in strs:
            sort = "".join(sorted(string))
            if sort in hsh:
                hsh[sort].append(string)
            else:
                hsh[sort] = [string]

            
        for thing in hsh.values():
            arr.append(thing)

        return arr

        