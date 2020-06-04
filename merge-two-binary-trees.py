class Solution:
  def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    
    root = self.recursive(t1,t2)
    
    return self.iterative(t1,t2)
  
  def iterative(self,t1,t2):
    if t1 is None:
      return t2
    stack, root = [[t1,t2]], t1
    
    while stack:
      pair = stack.pop()
      
      if pair[0] is None or pair[1] is None:
        continue
      
      pair[0].val += pair[1].val
    

      
      if pair[0].left is None:
        pair[0].left = pair[1].left
      else:
        stack.append([pair[0].left,pair[1].left])
      
      if pair[0].right is None:
        pair[0].right = pair[1].right
      else:
        stack.append([pair[0].right, pair[1].right])
        
    return t1
  def recursive(self,t1, t2):
    if t1 is None:
      return t2
    if t2 is None:
      return t1
    if t2 is None and t1 is None:
      return
    
    newVal = t1.val + t2.val
    root = TreeNode( val = newVal)
    root.left = self.recursive(t1.left, t2.left)
    root.right = self.recursive(t1.right, t2.right)
    
    return root
