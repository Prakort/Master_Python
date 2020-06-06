class Solution:
  ''' simple and beautiful solution
  preorder = [3,9,20,15,7]
  inorder = [9,3,15,20,7]
  3 is the root from the preorder
  3 in inorder array divide into 2 sub
  9 is the left subtree and 15,20,7
  we could apply this recursively on each subtree to get Binary Tree
  by finding get the indexing of the first element in preorder 
  and seperating the subtree
  Run Complexity: O(n) every node is visited
  Space Complexity: O(n) we use O(n) to place the function on the stacks
  '''
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
      index = inorder.index(preorder.pop(0))
      root = TreeNode(inorder[index])
      root.left = self.buildTree(preorder, inorder[0:index])
      root.right = self.buildTree(preorder, inorder[index + 1:])
      return root
      