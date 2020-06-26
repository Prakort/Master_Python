class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
      
      def dis(a):
          return sqrt(a[0]**2 + a[1]**2)
      
      deck = []
      
      for n in points:
          deck.append((dis(n),n))
  
      deck.sort(key= lambda x: x[0])
      res = []
      while K > 0 :
          res.append(deck[0][1])
          deck = deck[1:]
          K -= 1
          
      return res
      