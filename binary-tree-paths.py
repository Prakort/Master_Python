def solution(root):
  """
      7
    3   3
  1 

  7->3
  7->3->1
  print all possible paths

  Method: BSF, get node value level by level and add into the path
  when it is a leaf, add the path into the result
  """

  if not root:
    return []
  stack, res = [(root, str(root.val)], []

  while stack:
    node, path = stack.pop()
    if node:
      if not node.right and not node.left:
        res.append(path)

      if node.right:
        stack.append((node.right, path + '->' + str(node.right.val)))
      if node.left:
        stack.append((node.left, path + '->' + str(node.left.val)))

def recursive(root, path, ans):
  if not root:
    return 

  path += str(root.val)
  if not root.left and not root.right:
    ans.append(path)
    return 
  path += '->'
  recursive(root.left, path, ans)
  recursive(root.right, path, ans)

  

  