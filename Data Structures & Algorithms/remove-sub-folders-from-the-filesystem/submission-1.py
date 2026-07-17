class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.trie = TrieNode()

    def add(self, string):
        trie = self.trie
        i = 1

        while i < len(string):
            char = string[i]
            if char not in trie.children:
                trie.children[char] = TrieNode()

            trie = trie.children[char]
            i += 1

        trie.end = True


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        tree = PrefixTree()

        for f in folder:
            tree.add(f.split('/'))

        res = []

        def dfs(child, s):
            root = child
            for i, j in root.children.items():
                new_s = s + '/' + i
                if j.end:
                    res.append(new_s)
                    continue
                else:
                    dfs(j, new_s)
        
        dfs(tree.trie, "")
        return res
            


        

        


        
        




        


        