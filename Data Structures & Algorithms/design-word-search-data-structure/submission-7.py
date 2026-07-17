class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):

        self.trie = TrieNode()

    def addWord(self, word: str) -> None:

        trie = self.trie

        for char in word:
            if char not in trie.children:
                trie.children[char] = TrieNode()
            trie = trie.children[char]

        trie.word = True

    def search(self, word: str) -> bool:
        """
        return true if there is any string in the data structure that matches word - simple

        dots can be matched with any letter - essentially a wild card


        """

        def dfs(j, child):
            trie = child
            for i in range(j, len(word)):
                char = word[i]

                if char == ".":
                    for child in trie.children.values():
                        if dfs(i + 1, child):
                            return True

                    return False

                else:
                    if char not in trie.children:
                        return False

                    trie = trie.children[char]

            return trie.word

        return dfs(0, self.trie)
