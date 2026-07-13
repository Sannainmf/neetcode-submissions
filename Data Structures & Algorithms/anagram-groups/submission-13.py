class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """loop through, sor
        
        t every element, if it is unique sort, add create a new sublist and add it, if it is not a unique sort, add it to the s
        ort that mathches with its sort"""

        hash = {}

        for i in strs:
            sortI = ''.join(sorted(i))

            if sortI in hash:
                hash[sortI].append(i)
            else:
                hash[sortI] = [i]
        
        return list(hash.values())
        