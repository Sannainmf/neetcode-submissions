class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """loop through, sor
        
        t every element, if it is unique sort, add create a new sublist and add it, if it is not a unique sort, add it to the sort that mathches with its sort"""
        hash = {}

        for word in strs:
            sortWord = ''.join(sorted(word))
            if sortWord in hash:
                hash[sortWord].append(word)
            else:
                hash[sortWord] = [word]

        return list(hash.values())