def solution(root):
    
  res = []
  dfs(root, res)
  
  return res

def dfs(root, res):
  if not root:
    return 
  
  if not root.right and not root.left:
    return 
  
  if not root.right and root.left:
    res.append(root.left.val)
  if not root.left and root.right:
    res.append(root.right.val)
    
  dfs(root.right,res)
  dfs(root.left,res)
            
def iterative(root):

  res, stack = [], [root]

  while stack:
    node = stack.pop()

    if node:
      if node.right and not node.left:
        res.append(node.right.val)
      if node.left and not node.right:
        res.append(node.left.val)

      stack.append(node.right)
      stack.append(node.left)
        