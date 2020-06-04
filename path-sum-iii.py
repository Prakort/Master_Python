class Solution:
  def pathSum(self, root: TreeNode, sum: int) -> int:
    if not root:
      return 0
    # why call pathSum on root.right and root.left
    # we want to check all the possible paths
    # not just from the root node
    # this will check the child node from 0 + carry
    # to get all possible paths
    return self.pathSum(root.right,sum) +  self.pathSum(root.left,sum) + self.recursive(root,0,sum)
      
  def recursive(self,root, carry, sum):
    
    if not root:
      return 0
    
    # check the carry + val is equal to sum 
    # apply the recursion on the subtree
    return (carry + root.val == sum) + self.recursive(root.right, root.val + carry, sum) + self.recursive(root.left, root.val + carry, sum)
    
  