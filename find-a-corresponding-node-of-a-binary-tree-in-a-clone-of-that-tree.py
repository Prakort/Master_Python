def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    
  return dfs(original, cloned, target)
  
def dfs(t1, t2, target):
  if not t1 or not t2:
    return None

  if t1 is target:
    return t2

  right = dfs(t1.right, t2.right, target)
  left = dfs(t1.left, t2.left, target)
  return right if right else left

def iterative(original, cloned, target):
  t1 = [original]
  t2 = [cloned]
  while t1 and t2:
    node1 = t1.pop()
    node2 = t2.pop()
    
    if node1 is target:
      return node2
    
    if node1 is not None:
      t1.append(node1.left)
      t1.append(node1.right)
    if node2 is not None:
      t2.append(node2.left)
      t2.append(node2.right)
      
    