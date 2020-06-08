def iterative(l1, l2):

  node = TreeNode(0)
  dummy = node 

  while l1 and l2:
    if l1.val < l2.val:
      node.next = l1
      l1 = l1.next

    else:
      node.next = l2
      l2 = l2.next

    node  = node.next
  return dummy.next

def recursive(l1, l2):
  if not l1:
    return l2
  if not l2:
    return l1

  if l1.val < l2.val:
    # since l1 is smaller, we return l1 node
    # we want to find the next node by comparing l1.next and l2
    l1.next = recursive(l1.next, l2)
    return l1
  else:
    l2.next = recursive(l1, l2.next)
    return l2

  
