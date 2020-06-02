def hasCycle1(self, head: ListNode) -> bool:
  s = set()
  while head != None:
    if head in s:
      return True
    s.add(head)
    head = head.next
  return False
  
def hasCycle2(self, head: ListNode) -> bool:
  slow = head
  fast = head
  while slow and fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
    if(slow == fast):
      return True
  return False
