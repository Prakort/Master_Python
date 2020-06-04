class Solution:
  def invertTree(self, root: TreeNode) -> TreeNode:
    
    return self.recursive(root)


  # pass parent node in arg
  # swap the children the parent node
  # apply recursive to the child node as the parent of their own nodes


  # Complexity: each node is the tree is visited only once
  # time complexity is O(n) where n is the number of the nodes in the tree
  # This is recursive function, the function will be places on the stack
  # in the worst case, where H is the height of the tree then
  # space complexity is O(H)
  def recursive(self,root):
    if root is None:
      return 
    root.left, root.right = root.right, root.left
    self.recursive(root.right)
    self.recursive(root.left)
    
    return root
      
    
  # time and space complexity are O(n) 
  # everyone node is visited and we use a stack to store all the nodes to swap their children
  def iterative(self,root):
    stack = [root]
    while stack:
      node = stack.pop()
      if node is not None:
        node.right, node.left = node.left, node.right
        if node.right:
          stack.append(node.right)
        if node.left:
          stack.append(node.left)
        
    return root
