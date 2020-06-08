class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    return self.intersection(headA, headB)
  def intersection(self, headA, headB):
    
    A = headA
    B = headB
    
    # if they are the same we found the intersection
    # if they are both Null, they reached the end of the list
    # list A + list B = list B + list A, sum of both length are the same
    # A and B will reach Null if we dont find an intersection
    while A is not B:
      A = A.next if A else headB
      B = B.next if B else headA
      
    return A
  def iterativeNspace(self, headA, headB):
    s = []
    while headA:
      s.append(headA)
      headA = headA.next
      
    print('none == none', None is None)
    while headB:
      if headB in s:
        return headB
      headB = headB.next
      
      
    return None
  def iterative(self, headA, headB):

    while headA:
      # reset the list by since we iterate to the end of the headB list
      # this will restart the second list from the beginning again
      curr = headB
      while curr:
        if headA is curr:
          return headA
        curr = curr.next
      headA = headA.next
      
    return None
