def deepestLeavesSum(self, root: TreeNode) -> int:
    sum_total = 0
    res = []
    
    self.bfs(root, 0, res)
    print('sum',res[len(res)-2])
    return self.iterative(root)
  
def iterative(self, root):
  
  stack = deque([root,])
  
  while stack:
    level = stack
    stack = deque()
                
    for node in level:
      if node.left:
        stack.append(node.left)
      if node.right:
        stack.append(node.right)
        
  return sum([node.val for node in level])
    
    
def bfs(self, root, level, res):
  if level == len(res):
    res.append([])
    
  if root:
    res[level].append(root.val)
    self.bfs(root.right, level + 1, res)
    self.bfs(root.left, level + 1, res)
