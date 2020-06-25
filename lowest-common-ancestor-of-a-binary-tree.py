def iterative(root, p, q):
  """
  Our to goal to find the lowest common ancestors,
  the child could can be a descendant of itself
  
  Fact, q and p must not be null
  Fact, tree is not null
  Fact, binary is just regular binary tree
  
  Idea: 
  -store all the mapping/relationship as child -> parent 
  for all pairs up to q and p
  -since we have the mapping, we could find all the ancestors of p
  we going from bottom up until root
  -finally, we do same for q, find its ancestor one by one while check if 
  one of the ancestors is already in p ancestors set
  
  """

  stack, p_ancestors, mapping = [root], set(), {root: None}
  # get all ancestors of p and q in the mapping in term child->parent
  while q not in mapping or p not in mapping:
    node = stack.pop()
    if node:
      if node.left:
        mapping[node.left] = node 
        stack.append(node.left)
      if node.right:
        mapping[node.right] = node 
        stack.append(node.right)

  # let's find all possible ancestors of p
  cur = p
  while cur:
    p_ancestors.add(cur)
    # get the next ancestor
    cur = mapping[cur]

  # we have p ancestors 
  cur = q 
  # if we dont find common ancestor, cur is root -> None ==> cur = None
  while cur not in p_ancestors:
    cur = mapping[cur]
  
  return cur



def recursive(root, p, q):
  """
  If a subtree has one of the node q or p, mark as 1,
  then if a parent has both q and p, sum >= 2
  since we cound a parent as its node descendant
  
  - keep recursive find the q and p, return the value and evaluate the total sum
  """
  if not root:
    return 0
  right = recursive(root.right, p , q)
  left = recursive(root.left, p, q)
  parent = 1 if (root is p or root is q) else 0
  
  if right + left + parent == 2:
    self.result = root
    
  return right or left or parent
