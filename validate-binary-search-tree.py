class Solution:
  def isValidBST(self, root: TreeNode) -> bool:
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
