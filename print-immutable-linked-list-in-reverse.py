# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

def recursive(head):
  if not head:
    return 
  
  recursive(head.getNext())
  head.printValue()

def iterative(head):
  stack = []
  while head:
    stack.append(head)
    head = head.getNext()
  while stack:
    stack.pop().printValue()
  
