class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest = strs[0]
        res = ""

        for string in strs:
            if len(string) <= len(shortest):
                shortest = string

        for i in range(len(shortest)):
            for string in strs:
                if string[i] != shortest[i]:
                    return res
                
            res += shortest[i]

        return res




        