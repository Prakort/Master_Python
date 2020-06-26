class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        same idea as merge 2 sorted linkedlist, we have 2 BST, performe the inorder traversal
        we will get two sorted arrays
        
        using One Pass method: check which first index is smaller, 
        then pop it and add into the result, WE ARE NOT POPPING BOTH at the same. 
        
        we dont care if they have the same size
        """
        r1, r2, res = deque(), deque(), []
        # get the sorted arrays
        self.helper(root1, r1)
        self.helper(root2, r2)
        
        # perfome merging
        while r1 or r2:
            # use float('inf') to mark the empty list
            # so when we need to pop, we dont pop an empty list
            x = r1[0] if r1 else float('inf')
            y = r2[0] if r2 else float('inf')
            # both list are empty
            if x is float('inf') and y is float('inf'):
                break
            # check which one to add into the list first
            # if one is float, that list is empty
            if y < x :
                res.append(r2.popleft())
            else:
                res.append(r1.popleft())
        return res
    
    def helper(self, root, res):
        if not root:
            return
        # keep traverse to the bottom left
        self.helper(root.left, res)
        # add value into the list
        res.append(root.val)
        # traverse right
        self.helper(root.right, res)
