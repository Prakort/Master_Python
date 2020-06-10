def solution(head, n):
  """
  goal is the drop the node at index n from the end
  prev-node (index n - 1 ).next = prev-node.next.next 
  n is the index from the right but we dont know the length of the linkedlist
  ***len(list) - n + 1 is the target index from the left (1)
  
  use two iterators to keep track the index
  ahead = advances one node a time until the end of the list
  ahead -> the end ==> # steps = len(list) 
  ***let ahead = len(list) (2)

  prev = advances one node only when ahead iterator reaches and passes the target node! Why ?
  
  by (1) target-node index:= len(list) - n + 1
  then the prev node index:= len(list) - n 
  
  by (2) ahead = len(list) then ==> prev = ahead - n
  How do we know when to start advancing prev ?
  
  prev = ahead - n ==> the first index is 1 then which is ahead index that makes prev = 1? ==> ahead := n + 1
  
  from [n + 1.... len(list)] the end of the list we should advance prev iterator
  
  """
  dummy = ListNode(-1)
  ahead = dummy.next
  prev = dummy.next
  count = 0
  while ahead:
    if count >= n + 1:
      prev = prev.next

    count += 1
    ahead = ahead.next 

  if prev:
    prev.next = prev.next.next 

  return dummy.next

