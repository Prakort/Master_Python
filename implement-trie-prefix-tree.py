class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:

    def __init__(self):
        self.root = Node()
        """
        Initialize your data structure here.
        """
        

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
        node.end = True
        

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)
    def dfs(self, node, word):
        for i,w in enumerate(word):
            if w not in node.children:
                return False
            node = node.children[w]
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
            
        return True
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
