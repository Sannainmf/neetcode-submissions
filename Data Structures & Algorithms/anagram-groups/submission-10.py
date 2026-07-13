class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """loop through, sor
        
        t every element, if it is unique sort, add create a new sublist and add it, if it is not a unique sort, add it to the s
        ort that mathches with its sort"""

        hash = {}

        for i in strs:
            sortI = tuple(sorted(i))

            if sortI not in hash:
                hash[sortI] = [i] 
            else:
                hash[sortI].append(i)

        return list(hash.values())

        