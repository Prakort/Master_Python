class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
      # key: old node, value: copied of the old node
      hm = {}
      
      return self.recursive(head, hm)
    '''
    we have a linkedlist where a node has a next pointer and a random pointer, we could treat the list as a graph where we will process copying each node as a depth first
    
    since there exists a random pointer, it could cause an infinite loop e.g node 4 .next is node 7 and node 7 . random is 4 
    
    to prevent this infinite loop, we could use a hasmap to store the
    key/value where key = old node and value = copied version
    
    1-first we check if the node has been processed/copied already in the hashmap, if yes, return that cloned version, otherwise we create a new copy of that current node
    
    2-add the new copied version into the hashmap to prevent the loop
    
    3-after creating a new node, find the new node.next and new node.random respectively to the old node.next and old.node.random 
    ( this step might will perform the DFS until the end of the list and some functions call will just return the cloned version that has been processed already)
    
    4- return the new copied version
    
    '''
    def recursive(self,head,hm):
      if not head:
        return head
      
      # check if the node has been processed
      if head in hm:
        return hm[head] # return the copy version 
      
      node = Node(head.val)
      
      hm[head] = node
      
      node.next = self.recursive(head.next)
      node.random = self.recursive(head.random)
      
      return node
      
    def iterative(self,head):
      if not head:
        return head

      curr = head
      while curr:
        # create a new node
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        # move to the next old node
        curr = new_node.next
      
      # connect the random node of the copy version
            
      # connect the random point of the copied nodes
      # example:
      # A->A'->B->B'->C->C'
      # A next is A'
      # A random is C (1)
      # C next is C' (2)
      # A next random is A' random (3)
      # A next random := A random next
      # by (1) and (2) A random next = C' (4)
      # by (3) and (4) A' random = C'
      # this is exactly what we want A random is C and A' random is C'

      curr = head
      while curr:
        curr.next.random = curr.random.next if curr.random else None
        curr = curr.next.next

      l1 = head
      l2 = head.next 
      ptr = head.next

      # A->A'->B->B' 
      # A next  = A' next next = B
      # A' next = B next next = B'
      while l1:
        l1.next = l1.next.next if l1.next else None
        l2.next = l2.next.next  if l2.next else None

        l1 = l1.next 
        l2 = l2.next


      return ptr
      
    
    def simpleIterative(self,head):
      if not head:
        return head
      
      def cloneNode(head,hm):
        if not head:
          return head 

        if head in hm:
          return hm[head]
        else:
          node = Node(head.val)
          hm[head] = node 
          return node

      hm = {}
      copy = cloneNode(head,hm)

      while head:

        copy = cloneNode(head,hm)
        # not check head ? because while head has already checked if head is null or not 
        # no need to check it again
        copy.next = cloneNode(head.next, hm)
        copy.random = cloneNode(head.random, hm)

        head, copy = head.next, copy.next 
        

