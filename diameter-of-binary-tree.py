class Solution:
  def diameterOfBinaryTree(self, root: TreeNode) -> int:
      
    # every node is visited => time complexity is O(n)
    # recursive function is placed on the stack 
    # which the heigh of the tree is H <= n => space complexity is O(n)
    def findDepth(root):
      if not root:
        return 0
      # find the number of step from root to left/right child
      left = findDepth(root.left) 
      right = findDepth(root.right) 
      # update the diameter with left + right + 1 
      # + 1 is the root node since it is not null
      # left is number of nodes from the left subtree
      # right is number of nodes from the right subtree
      self.dia = max(self.dia, left + right  + 1)
      
      return max(left,right) +1
    
    self.dia = 0
    if root is None:
      return 0
    findDepth(root)
    
    # why -1 ? since we find the best steps between
    # the deepest leafs, the result we want is length
    # not steps, so we want to minus 1
    # e.g A->B->C steps: 3 but length is 2
    
    return self.dia - 1
