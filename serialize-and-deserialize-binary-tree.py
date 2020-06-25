class Codec:
  """
  we have a binary tree, 
  we want to find a way that's easy to write and rebuild the tree
  the easiest way is inorder traversal
  read all nodes inorder store them in list => convert into string with ','
  """
  def inorder(self, root, ans):
    
      if not root:
        ans.append('#')
        return
      ans.append(str(root.val))
      self.inorder(root.left, ans)
      self.inorder(root.right, ans)

  def serialize(self, root):
      ans = []
      self.inorder(root, ans)
    
      return ','.join(ans)
      

  def deserialize(self, data):
      # this is why I started to love deque()
      # no need to handle with index
      nodes = deque(data.split(','))
      root = self.buildTree(nodes)
      return root
    
  def buildTree(self, data):
      """
      let's build the tree from inorder list
      get the value if is not '#', convert to node find node.right and node.left
      if value is '#' return None, dont forget to always pop the value
      """
      if data[0] == '#':
        data.popleft()
        return None
      
      value = data.popleft()
  
      node = TreeNode(value)
      node.left = self.buildTree(data)
      node.right = self.buildTree(data)
  
      return node
      