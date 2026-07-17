class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        cur = self.root

        for c in w:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]
            cur.count += 1

    def count(self, w):

        cur = self.root

        for c in w:
            if c not in cur.children:
                return 0
            cur = cur.children[c]

        return cur.count
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        tree = PrefixTree()

        for w in words:
            if len(w) >= len(pref):
                tree.add(w)

        return tree.count(pref)





        