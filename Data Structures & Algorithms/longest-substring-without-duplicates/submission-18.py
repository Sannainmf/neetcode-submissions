class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

    #have left and r pointer, add each r pointer to a set, if one is a rpeeat remove the one
    # in set and add the current, track longest everytime you add a char

        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, len(charSet))

        return res






        