def hasCycle1(self, head: ListNode) -> bool:
  s = set()
  while head != None:
    if head in s:
      return True
    s.add(head)
    head = head.next
  return False
  
def hasCycle(self, head: ListNode) -> bool:
  slow = head
  fast = head
  
  # if slow is null ==> the end of the list
  # if fast is null ==> the end of the list
  # if fast.next is null ==> fast is the last node of the list
  while slow and fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:
      return True
    
    
  return False
  

