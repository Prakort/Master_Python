class Solution:
  def pathSum(self, root: TreeNode, sum: int) -> int:
    if not root:
      return 0
    
    hm = {0:1}
    
    return self.helper(root,0,sum,hm)
    # why call pathSum on root.right and root.left
    # we want to check all the possible paths
    # not just from the root node
    # this will check the child node from 0 + carry
    # to get all possible paths
    # return self.pathSum(root.right,sum) +  self.pathSum(root.left,sum) + self.recursive(root,0,sum)
      
  def recursive(self,root, carry, sum):
    
    if not root:
      return 0
    
    # check the carry + val is equal to sum 
    # apply the recursion on the subtree
    return (carry + root.val == sum) + self.recursive(root.right, root.val + carry, sum) + self.recursive(root.left, root.val + carry, sum)
  
  def helper(self, root,carry, target, hm):
    if not root:
      return 0
    # add carry with node val
    carry += root.val
    # find the occurrence of the pre sum index 
    # the target - carry = pre sum index that we store 
    occur = hm.get(carry - target) if (carry - target) in hm else 0
    
    # update the map with the calucated sum
    hm[carry] =  1 if hm.get(carry) is None else hm.get(carry)+1
    # find all possible path that will add up to the sum
    res= occur + self.helper(root.right,carry,target,hm) + self.helper(root.left, carry, target, hm)
    # restore the map by reducing the occurrence of the sum
    hm[carry] =  hm.get(carry) - 1 
    return res



