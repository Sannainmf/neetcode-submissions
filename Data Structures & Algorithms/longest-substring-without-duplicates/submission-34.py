class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        longest = 0
        arr = []

        for r in range(len(s)):

            while s[r] in arr:
                arr.remove(s[l])
                l += 1

            arr.append(s[r])
            longest = max(longest, len(arr))
            r += 1
        
        return longest
            
                
        



            




        