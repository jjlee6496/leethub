class Solution(object):
    def __init__(self):
        self.primes = self.generate(1000)
    
    @staticmethod
    def generate(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if primes[i]:
                for j in range(i*i, limit+1, i):
                    primes[j] = False
        return [i for i in range(limit, 1, -1) if primes[i]]

    def bs(self, target, prev):
        l, r  = 0, len(self.primes) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            prime = self.primes[mid]

            if prime >= target:
                l = mid + 1
            else:
                if target - prime > prev:
                    res = prime
                    r = mid - 1
                else:
                    l = mid + 1
        return res

    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        
        prev = 0
        for i in range(n):
            prime = self.bs(nums[i], prev)
            if prime != -1:
                nums[i] -= prime

            if nums[i] <= prev:
                return False
            
            prev = nums[i]
        return True