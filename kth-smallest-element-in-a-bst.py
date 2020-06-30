class Solution:
  # using BST property to solve this
  # BST nodes are sorted
  # inorder traversal will get the kth smallest element
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    stack, curr, result = [], root, []
    
    while curr or stack:
      while curr:
        stack.append(curr)
        curr = curr.left
        
      curr = stack.pop()
      result.append(curr.val)
      curr = curr.right
      
      if len(result) == k :
        return result[k-1]
  
  def recursive(self, root, res):
      if not root:
        return 
      self.recursive(root.left,res)
      res.append(root.val)
      self.recursive(root.right,res)
      