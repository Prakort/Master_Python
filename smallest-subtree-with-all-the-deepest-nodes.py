def solution(root):
  """ 
        5
      1   2
    3
    answer: 3
        5
      1   2
        3
    answer: 3
        5
      1   2
    3   4
    answer: 4

    if the node is the has largest depth then it is the answer
    if two nodes have the has largest depth then return their parent
    
    Method: dfs, recursive

    We want pass down the node and depth from ROOT and O and keep
    increment the depth + 1 each child, until Null node and return None,Depth

    we have to check right and left node to find the largest depth 
    compare both of them by using above rules

    return the largest max node

  """
  def dfs(root, depth):
    #base case
    if not root:
      return [None,depth]

    # check right and left subtree 
    # increment the depth
    right = dfs(root.right, depth + 1)
    left = dfs(root.left, depth + 1)
    # follow the rule, if both left and right child are the max, return the parent
    if right[1] == left[1]:
      return [root,left[1]]
    # return only the max node to the top 
    if right[1] > left[1]:
      return right
    else:
      return left

