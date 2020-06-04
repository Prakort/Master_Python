class Solution:
  def maxDepth(self, root: TreeNode) -> int:
      
      return self.hieght(root)
  
  def height(self,root):
        
        if root is None:
          return 0
        
        #find the left subtree height
        left = self.height(root.left)
        #find the right subtree height
        right = self.height(root.right)
        
        # why + 1 ? one is the root node since we already check it is not null
        return max(left,right) + 1
        