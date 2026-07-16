class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        count = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                l = words[i]
                r = words[j]

                prefix = False
                suffix = False

                if l == r[ : len(l)]:
                    prefix = True

                if l == r[len(r) - len(l) : ]:
                    suffix = True

                if prefix and suffix:
                    count += 1

        return count




        