class Solution:
  def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    self.helper(root)
      
  def helper(self,root):
    
    if not root:
      return None
    
    if not root.right and not root.left:
      return root
  
    left = self.helper(root.left)
    
    right = self.helper(root.right)
    
    if left:
      left.right = root.right
      root.right = root.left
      root.left = None
      
    return right if right else left
