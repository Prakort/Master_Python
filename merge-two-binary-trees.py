class Solution:
  def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    
    root = self.recursive(t1,t2)
    
    return self.iterative(t1,t2)
  
  def iterative(self,t1,t2):
    if t1 is None:
      return t2

    stack= [[t1,t2]]
    
    while stack:
      pair = stack.pop()
      # if t2 node is null, we skip to the next iteration
      # since we already check the t1 node existence before adding into the stack
      if pair[1] is None:
        continue
      # t1 and t2 are not null, add their value together
      pair[0].val += pair[1].val
  
      # if the t1 child is null, t1 child will take val of the t2 child, both as right/left
      if pair[0].left is None:
        pair[0].left = pair[1].left
      else:
        # otherwise, add the pair into the stack and evaluate them
        stack.append([pair[0].left,pair[1].left])
      
      if pair[0].right is None:
        pair[0].right = pair[1].right
      else:
        stack.append([pair[0].right, pair[1].right])
        
    return t1

  # we want to recursively compare both t1 and t2 tree
  # by checking each children of each trees respectively
  def recursive(self,t1, t2):
    
    if t1 is None:
      return t2
    if t2 is None:
      return t1
    if t2 is None and t1 is None:
      return
    # when both nodes are not null
    # add the values together
    # find the new children of the new node by calling the recursive function on a pair t1 and t2 left/right respectively
    newVal = t1.val + t2.val
    root = TreeNode( val = newVal)
    root.left = self.recursive(t1.left, t2.left)
    root.right = self.recursive(t1.right, t2.right)
    
    # return the new node
    return root
