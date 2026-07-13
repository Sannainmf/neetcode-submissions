class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in s[l : r]:
                l += 1

            longest = max(longest, len(s[l : r]) + 1)

        return longest






                
