class solution:
  def rob(self,root):
    if not root:
      return 0
    return self.helper(root)

  # time complexity is O(n) all the nodes are visited once
  # space complexity is O(n) since the function will be places on stack where h is the height <= n nodes
  def helper(self,root):
    if not root:
      return (0,0)

    rob_left_child, skip_left_child_rob_left_childs_nodes = self.helper(root.left)
    rob_right_child, skip_righ_child_rob_right_childs_nodes = self.helper(root.right)
    # 1st element: rob the parent nodes and the child nodes' nodes
    # 2nd element: maximum between all possible paths
    return (root.val + skip_left_child_rob_left_childs_nodes + skip_righ_child_rob_right_childs_nodes, max(
      rob_left_child + rob_right_child,
      rob_left_child + skip_righ_child_rob_right_childs_nodes,
      rob_right_child + skip_left_child_rob_left_childs_nodes,
      skip_left_child_rob_left_childs_nodes + skip_righ_child_rob_right_childs_nodes
    ))
