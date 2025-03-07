class Solution(object):
    sieve = [True] * (10 ** 6 + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, 10 ** 3 + 1):
        if sieve[i]:
            for j in range(i * i, 10 ** 6 + 1, i):
                sieve[j] = False
        
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        primes = [i for i in range(left, right + 1) if self.sieve[i]]
        closest = [-1, -1]
        if len(primes) < 2:
            return closest

        min_diff = float('inf')
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                closest = [primes[i - 1], primes[i]]
        return closest