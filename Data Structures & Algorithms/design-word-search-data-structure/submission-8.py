class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:

        trie = self.trie

        for char in word:
            if char not in trie.children:
                trie.children[char] = TrieNode()

            trie = trie.children[char]

        trie.end = True
        

    def search(self, word: str) -> bool:

        def dfs(j, root):
            for i in range(j, len(word)):
                char = word[i]

                if char == ".":
                    for child in root.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
            
                else:
                    if char not in root.children:
                        return False
                    else:
                        root = root.children[char]

            if root.end:
                return True

            return False

        return dfs(0, self.trie)


        
