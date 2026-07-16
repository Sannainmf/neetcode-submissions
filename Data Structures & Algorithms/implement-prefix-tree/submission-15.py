class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        
        self.trie = TrieNode()

    def insert(self, word: str) -> None:

        trie = self.trie

        for char in word:
            if char not in trie.children:
                trie.children[char] = TrieNode()
            
            trie = trie.children[char]

        trie.end = True


    def search(self, word: str) -> bool:

        trie = self.trie

        for char in word:
            if char not in trie.children:
                return False
            
            trie = trie.children[char]

        if trie.end == True:
            return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:

        trie = self.trie

        for char in prefix:
            if char not in trie.children:
                return False
            
            trie = trie.children[char]

        return True
        
        