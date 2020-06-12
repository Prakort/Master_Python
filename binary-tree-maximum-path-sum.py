def solution(root):
  self.max = 0

  recursion(root)

  return self.max

def recursion(root):
  if not root:
    return 0 

  left = max(recursion(root.left), 0)
  right = max(recursion(root.right), 0)

  self.max = max(left + right + root.val , self.max)

  return root.val + max(left,right)

