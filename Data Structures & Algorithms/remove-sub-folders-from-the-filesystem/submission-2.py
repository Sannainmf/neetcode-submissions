class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def add(self, folder):

        trie = self.trie
        i = 1

        while i < len(folder):
            char = folder[i]
            if char not in trie.children:
                trie.children[char] = TrieNode()
            
            trie = trie.children[char]
            i += 1

        trie.end = True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        tree = PrefixTree()

        for f in folder:
            s = f.split("/")
            tree.add(s)

        arr = []

        def dfs(root, string):
            t = ""
            for i, j in root.children.items():
                t = string + '/' + i

                if j.end:
                    arr.append(t)
                    t = ""
                    continue
                else:
                    dfs(j, t)

            return arr

        return dfs(tree.trie, "")




                
                

        