class Solution:
  def invertTree(self, root: TreeNode) -> TreeNode:
    
    return self.recursive(root)
  # pass parent node in arg
  # swap the children the parent node
  # apply recursive to the child node as the parent of their own nodes
  def recursive(self,root):
    if root is None:
      return 
    root.left, root.right = root.right, root.left
    self.recursive(root.right)
    self.recursive(root.left)
    
    return root
      
    
     