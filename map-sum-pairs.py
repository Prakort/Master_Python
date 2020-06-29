class Trie():
  def __init__(self):
    self.children = {}
    self.value = 0

class MapSum:

  def __init__(self):
    self.map = {}
    self.root = Trie()

  def insert(self, key, value):
    diff = value - self.map.get(key, 0)
    cur = self.root
    cur.value += diff 

    for ch in key:
      if ch not in cur.children:
        cur.children[ch] = Trie()

      cur = cur.children[ch]

  def sum(self, prefix):
    cur = self.root
    for ch in prefix:
      if ch not in cur.children:
        return 0
      cur = cur.children[ch]
    return cur.value
