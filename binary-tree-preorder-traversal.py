class TreeNode:
  def __init__(self,right = None, left= None , val = 0):
    self.right = right
    self.left = left
    self.val = val

def preorder_traversal(root : TreeNode ,list):

  if root is None:
    return
  list.append(root.val)

  if root.left:
    preorder_traversal(root.left,list)
  if root.right:
    preorder_traversal(root.right,list)

def preorder_traversal_stack(root):
  stack, result = [root], []
  while stack:
    node = stack.pop()
    root.append(node.val)

    # we use stack first in last out 
    # add the right child before the left child 
    # we will pop the left node first
    if node.right:
      stack.push(node.right)

    if node.left :
      stack.push(node.left)


def solution(root: TreeNode):
  list = []
  preorder_traversal(root,list)
  return list

root = TreeNode(val = 4)
root.right = TreeNode(val = 5)
root.left = TreeNode(val= 3)
# stack = [root]
# for i in stack:
  
