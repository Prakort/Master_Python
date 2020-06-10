def solution(l1, l2):
  """
  add the value of l1 and l2 if they are not null
  create a new node of the sum and check for carry
  assign the new node to connect with the list 
  iterate to the next node for curr, l1 , l2

  final step to check the carry again 
  if carry > 0, then we need to create a new node for the last carry

  """
  curr = ListNode(0)
  dummy = curr
  carry = 0

  while l1 or l2:
    # find the sum
    sum = carry 
    sum += l1.val if l1 else 0
    sum += l2.val if l2 else 0
    # get the carry
    carry = sum // 10
    # create a new node for the sum less then 10
    curr.next = ListNode(sum % 10)
    # prepare for next iteration
    curr = curr.next 
    l1, l2 = l1.next if l1 else None, l2.next if l2 else None

  # check carry value again 
  if carry > 0:
    curr.next = ListNode(carry)

  return dummy.next

