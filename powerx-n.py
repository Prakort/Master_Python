class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
      
        return self.nlogn_iterative2(x, n)
    def nlogn(self,x ,n):
        """
        x^n = x^(2(n/2)) if n is even 
        x^n = x^(2(n-1)/2) if n is odd
        we could apply x as base and n as binary like 13 => 1101
        2 ** 13 
        if we keep diving n/2,we will have a tree structor like. The time complexity is just O(Height)
        which is O(logn)
        
        same as well with the space complexity where O(logn) is the depest recursion of the stacks
        
        """
        if n == 0:
            return 1
      
        if n % 2 == 0:
            return self.nlogn(x * x, n // 2)
        else:
            return x * self.nlogn(x * x, (n - 1 ) // 2)
    def nlogn_iterative(self, x, n):
        if n == 0:
            return 1
        y = 1
        """
        N = 9 ==> 2^3 + 2^0 = 1001, we get the product from 1 which is odd N
        """
        while n > 1:
            if n % 2 == 0:
                x = x * x
                n = n //2
            else:
                y = x * y
                x = x * x
                n = (n-1) //2
        return x * y
    def nlogn_iterative2(self, x, n):
        if n == 0:
            return 1
        y = 1
        """
        N = 9 ==> 2^3 + 2^0 = 1001, we get the product from 1 which is odd N
        """
        while n > 0:
            if n % 2 == 1:
                # it is 1
                # update product
                y *= x                
            x *= x
            # move to the next left binary
            n //=2
             
        return y
    def iterative(self, x, n):
        if n < 0:
            n = -n
            x = 1/x
      
        res = 1
        cur = x
        i = n
        """
        
        
        """
        while i > 0:
            print('index', i)
            if i % 2 == 1:
                res *= cur
                print('res',res)
            cur *= cur
            print('cur', cur)
            i //=2
        
        return res
