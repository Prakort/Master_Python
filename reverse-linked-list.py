def iterative(head):

  prev = None
  curr = head
  nextNode = head

  # iterate until null node which is the end of the list
  while curr:
    # assign next node to the next node of the current node as a temp
    nextNode = curr.next

    # assign the current to the prev node
    # this will point the current node backward
    # that's what we wanted
    # why prev = None ? because this is the new end of the reversed linkedlist
    # but after first iteration, curr points back
    curr = prev

    # assign the prev to the current node
    prev = curr

    # update the curr to nextNode for the next iteration
    curr = nextNode
  # prev = curr til the curr is null that prev is the new head of the list
  return prev

def recursive(head):

  # if head is null ==> it is the end of the list
  # if the head.next is null ==> head is the last node of the list
  # we want to return that
  if not head or not head.next:
    return head
  # if head or head.next are not null
  # apply recursive function onto the head.next
  newHead = recursive(head.next)

  # when we point the head.next.next back the head 
  # we get the reversing pointer of the next node points to the previous
  head.next.next = head
  # since we need the first of the orginal list to point to null
  # we can point every node.next to None since the head.next.next points the head already
  # the job is done
  head.next = None

  # the last node of the old list will keep passing back to become the new head
  return newHead
