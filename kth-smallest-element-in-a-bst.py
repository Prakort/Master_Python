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
    