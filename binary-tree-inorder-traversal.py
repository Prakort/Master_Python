class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
      # in order left -> parent -> right 
    li = []
    self.recursive(root,li)
    return li 

  def recursive(self,root,li):
    if not root:
      return 
    # the left node will always add in first before the parent 
    if root.left:
      self.recursive(root.left, li)
    
    # left or right node value is added into the list only
    # it becomes the node that passed in the function
    li.append(root.val)

    # find the most left for right subtree
    if root.right:
      self.recursive(root.right, li)
    
    
  def iterative(self,root):  
    stack, result = [], []
    curr = root
    
    while curr or stack:
      # keep find the left most child
      while curr:
        stack.append(curr)
        curr = curr.left 
      
      curr = stack.pop()
      result.append(curr.val)
      curr = curr.right 
    return result
