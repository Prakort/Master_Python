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
    
  def recursive(root,list):
    if root is None:
      return
    recursive(root.left,list)
    recursive(root.right,list)
    list.append(root.val)
