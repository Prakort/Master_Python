def solution(root, target, K):
  # we could build a graph where a node points to all its parent and children
  # from the target, we travel level by level for K step
  # BFS approach

  graph = defaultdict(list)
  build(root, graph)

  res = []
  visited = set()
  q = deque((target.val, 0))

  while q:
    node, step = q.popleft()
    visited.add(node)
    if step == K:
      res.append(node)

    for n in graph[node]:
      if n not in visited:
        q.append((n, step+1))

  return res


def build(root, g):
  if not root:
    return 
  if root.left:
    g[root.left.val].append(root.val)
    g[root.val].append(root.left.val)
  if root.right:
    g[root.val].append(root.right.val)
    g[root.right.val].append(root.val)

  build(root.left)
  build(root.right)

