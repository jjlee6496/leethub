class Solution(object):
    def __init__(self):
        self.primes = self.generate(1000)
    
    @staticmethod
    def generate(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if primes[i]:
                for j in range(i+i, limit+1, i):
                    primes[j] = False
        return [i for i in range(limit, 1, -1) if primes[i]]

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
            for p in self.primes:
                if nums[i] > p and nums[i] - p > prev:
                    nums[i] -= p
                    break
            if nums[i] <= prev:
                return False
            prev = nums[i]
        return True