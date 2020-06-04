class Solution:
  def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
      return True
    return self.iterative(root)
  def helper(self,t1,t2):
    if not t1 and not t2:
      return True
    if not t1 or not t2:
      return False
    return t1.val == t2.val and self.helper(t1.right,t2.left) and self.helper(t1.left,t2.right)
  
  def iterative(self,root):
    # add pair(right child and left child) in the stack
    stack = [[root.right,root.left]]
    while stack:
      # get the pair to evaluate
      pair = stack.pop()
      left, right = pair[0], pair[1]
      # if they are null, skip to the next iteration
      if not left and not right:
        continue
      # otherwise one of them is null, return false
      if not left or not right:
        return False
      # if the values are not the same return false
      if left.val != right.val:
        return False
      # push the next pairs into the stack
      stack.append([left.left,right.right])
      stack.append([left.right,right.left])
      
    return True
      