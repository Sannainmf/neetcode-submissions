class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        arr = []
        longest = 0

        for r in range(len(s)):
            if s[r] not in arr:
                arr.append(s[r])
                longest = max(longest, len(arr))
            else:
                while s[r] in arr:
                    arr.remove(s[l])
                    l += 1
                arr.append(s[r])

        return longest

        