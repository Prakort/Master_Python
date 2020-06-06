class Solution:
  def isValidBST(self, root: TreeNode) -> bool:
    
    return self.recursive(root, float('-inf'), float('inf'))
  
  def recursive(self,root, min, max):
    if not root:
      return True
    # BST property that the values are sorted
    # check the lower and upper bound
    if root.val <= min or root.val >= max:
      return False

    # check the children node and update the lower and upper
    return self.recursive(root.right, root.val, max) and self.recursive(root.left, min, root.val)
  
  def iterative(self,root):
    # use stack to push the node
    stack, curr, smallest = [], root, float('-inf')
    
    while stack or curr:
      while curr:
        stack.append(curr)
        curr = curr.left

      curr = stack.pop()
      # check if the next node is greater than the last checked node
      if curr.val <=  smallest:
        return False
      # update the checked smallest
      smallest = curr.val
      curr = curr.right
      
    return True
