class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """loop through, sor
        
        t every element, if it is unique sort, add create a new sublist and add it, if it is not a unique sort, add it to the s
        ort that mathches with its sort"""

        hash = {}
        arr= []

        for word in strs:
            sortW = ''.join(sorted(word))

            if sortW in hash:
                hash[sortW].append(word)
            else:
                hash[sortW] = [word]

        for things in hash.values():
            arr.append(things)

        return arr
            
                