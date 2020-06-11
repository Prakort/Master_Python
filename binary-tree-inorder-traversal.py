class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack, result, curr = [], [], root
    while curr or stack:
      while curr:
        stack.append(curr)
        curr = curr.left
      curr = stack.pop()
      result.append(curr.val)
      curr = curr.right
    return result
    
  def recursive(self,root,list):
    if root is None:
      return
    if root.left:
      self.recursive(root.left,list)
    list.append(root.val)
    if root.right:
      self.recursive(root.right,list)
