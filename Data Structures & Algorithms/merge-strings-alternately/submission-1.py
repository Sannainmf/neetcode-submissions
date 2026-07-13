class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        smaller = ""
        longer = ""
        res = ""

        if len(word1) < len(word2):
            smaller = word1
            longer = word2
        else:
            smaller = word2
            longer = word1

        l = 0
        while l < len(smaller):
            res += word1[l]
            res += word2[l]
            l += 1

        res += longer[l:]
        return res


        