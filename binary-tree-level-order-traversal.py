"""
using curr to store the first node, we want to store the child of the parent in the same array because they are at the same level 

at first add the root.val into an array added into the result list
since we know the root exists

then assign a temporary list parents to hold the nodes 
then reset the curr list <= want to store all the child nodes
then reset the value list <= want to store the values of the child node

parents hold all the parent node, iterate through the list and add parent's child nodes into the curr and add their values into the value list 

next iteration, the value list will be added in the result list
and we reassign the parents list to the new child nodes from the previous iteration
"""
def levelOrder(root: TreeNode) -> List[List[int]]:
  # bread first search
  # we get the node each level 

  if not root:
    return []

  curr, value, result = [root], [root.val], []

  while curr:

    result.append(value)
    parents = curr
    curr, value = [], []

    for parent in parents:
      if parent.left:
        curr.append(parent.left)
        value.append(parent.left.val)
      if parent.right:
        curr.append(parent.right)
        value.append(parent.right.val)

  return result
def recursive(root, li, level):
  """
  every node that has the same level is added into the level index in the result list 
  
  why len(i) == level ? every time level + 1 and we need an extra array to put the new child nodes. Before every level, we will add a new empty list to hold the value preventing the out of index range
  """
  if len(li) == level:
    li.append([])

  li[level].append(root.val)
  if root.left:
    recursive(root.left, li , level + 1)
    
  if root.right:
    recursive(root.right, li, level +1 )
    
      
  
        
