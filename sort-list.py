def solution(head):
  
  return sort(head)

def sortList(head):
  
  # if node is null or node is the last node return that node
  if not head or not head.next:
    return head

  # our goal is to split the list into half until it is a single node and merge them back recursively

  # use slow pointer to keep track of the beginning of the second half
  slow = head
  # use fast pointer to get to the end of the list
  fast = fast
  
  # check only fast node , no need to check slow pointer
  while fast and fast.next and fast.next.next:
    # advance slow iterator one node
    slow = slow.next
    # advance fast iterator two nodes
    fast = fast.next.next

  # assign the the head of the second half, so we dont lose it before spliting the list
  secondHalf = slow
  # cut off the first half by assign slow.next = none
  slow.next = None

  firstHalf = sortList(head)
  secondHalf = sortList(secondHalf)

  # merge the 2 lists together
  return merge(firstHalf, secondHalf)

  
def merge(l1, l2):
  if not l1:
    return l2
  if not l2:
    return l1

  if l1.val < l2.val:
    l1.next = merge(l1.next, l2)
    return l1
  else:
    l2.next = merge(l1, l2.next)
    return l2
  
