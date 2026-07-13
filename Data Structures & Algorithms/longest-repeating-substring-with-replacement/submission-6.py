class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
#Basically, you have l and r pointer, and hasmap to count freq of letters (for max). longest. for r in range(len(s): you check the condition. ifif not validwe do l += 1, and weget rid of that thing by doing hasmpa remove that value.)

        count = {}
        l = 0
        longest = 0
        
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest