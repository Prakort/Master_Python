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
        
  def iterative(root):
        
    if not root:
      return 0
    
    stack = [(root,1)]
    height = 0
    while stack:
      node, level = stack.pop()
      height = max(height, level)
    
      if node.left:
        stack.append((node.left, level + 1))
        
      if node.right:
        stack.append((node.right, level + 1))
        
    return height
