class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.globe = set()
        

    def insert(self, val: int) -> bool:
        if val in self.globe:
            return False
        else:
            self.globe.add(val)
            return True
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        

    def remove(self, val: int) -> bool:
        if val not in self.globe:
            return False
        else:
            self.globe.remove(val)
            return True
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        

    def getRandom(self) -> int:
        l = [ _ for _ in self.globe]
        index = random.randint(0, len(self.globe) - 1)
        return l[index]

        """
        Get a random element from the set.
        """
