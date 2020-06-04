class Solution:
  def maxDepth(self, root: TreeNode) -> int:
      
      return self.hieght(root)
  
  def hieght(self,root):
    if root is None:
      return 0
    
    left = self.hieght(root.left) + 1
    right = self.hieght(root.right) + 1
    return max(left,right)
