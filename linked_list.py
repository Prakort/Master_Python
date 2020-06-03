# Linked Lists
# inserting and deleting element is O(1)
# get kth element is O(n)
class ListNode:
  def __init__(self, data=0, next_node = None):
    self.data = data
    self.next = next_node

  # O(n)
  def search_list(L, key):
    while L and L.data != key:
      L = L.next

    return L
  # O(1)
  def insert_after(node, new_node):
    node.next = new_node
    new_node.next = node.next

  # O(1)
  def delete_after(node):
    node.next = node.next.next



def swap(a,b):
  temp = a
  a = b
  b = temp
  return a,b

def swap(a,b):
  a = a^b 
  b = a^b
  a = a^b

  return a,n

