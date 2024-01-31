class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n<0:
            n = -n
            x = 1/x
        return self.pow_recursive(x, n)
        
    def pow_recursive(self, x, n):
        if n == 1:
            return x
        
        elif n%2==0:
            half_pow = self.pow_recursive(x, n//2)
            return half_pow*half_pow
        else:
            half_pow = self.pow_recursive(x, (n-1)//2)
            return x*half_pow*half_pow