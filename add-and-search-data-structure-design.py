class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    
    def __init__(self):
        self.root = TreeNode()
   
    def addWord(self, word: str) -> None:
        parent = self.root
        for c in word:
            if c not in parent.children:
                parent.children[c] = TreeNode()
            parent = parent.children[c]
            
        parent.end = True 
                
        """
        Adds a word into the data structure.
        """
        
    def dfs(self, root, word):
        for i in range(len(word)):
            if word[i] == '.':
                for k in root.children:
                    if self.dfs(root.children[k], word[i+1:]):
                        return True
                return False
            elif word[i] not in root.children:
                    return False
            else:
                root = root.children[word[i]]
        return root.end

    def search(self, word: str) -> bool:
    
        return self.dfs(self.root, word)
            
  