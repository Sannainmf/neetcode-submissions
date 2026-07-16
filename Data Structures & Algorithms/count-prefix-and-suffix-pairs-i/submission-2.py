class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        count = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                l = words[i]
                r = words[j]

                if r.startswith(l) and r.endswith(l):
                    count += 1

        return count




        