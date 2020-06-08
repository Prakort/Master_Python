def solution(head):
  if not head:
    return True

  slow = head
  fast = head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  # if fast is null, the length is EVEN, we need to move slow pointer to the next node
  # to split the list into even half
  # if fast.next is null, the length is ODD

  reverseHalf = reverse(slow if not fast else slow.next)

  while head and reverseHalf:
    if head.val != reverseHalf:
      return False

    head, reverseHalf = head.next, reverseHalf.next

  return True

def reverse(head):
  if not head or not head.next:
    return head

  newHead = reverse(head.next)
  head.next.next = head
  head.next = None

  return newHead
