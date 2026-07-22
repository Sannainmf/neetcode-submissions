class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        hsh = {}

        for i in range(len(words)):
            for j in range(len(words[i])):
                char = words[i][j]
                if char not in hsh:
                    hsh[char] = 1
                else:
                    hsh[char] += 1

        for c in hsh.values():
            if c % len(words) != 0:
                return False

        return True

        