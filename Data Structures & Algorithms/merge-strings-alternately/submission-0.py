class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        smallest = ""
        longest = "" 
        res = ""

        if len(word1) <= len(word2):
            smallest = word1
            longest = word2
        else:
            smallest = word2
            longest = word1

        index = 0

        for l in range(len(smallest)):
            
            res += word1[l]
            res += word2[l]
            index += 1

        return res + longest[index:]

        