class Solution:
    """
    for encoding, just do '#'.join(), reutrn that

    hello#world#areen

    return '#'.split()
    """

    def encode(self, strs: List[str]) -> str:

        string = ""

        for word in strs:
            string += str(len(word)) + '#' + word

        return string

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        start = 0

        while i < len(s):
            if s[i] == '#':
                digit = s[start:i]
                res.append(s[i + 1 : i + 1 + int(digit)])
                i = i + 1 + int(digit)
                start = i
            else:
                i += 1

        return res










