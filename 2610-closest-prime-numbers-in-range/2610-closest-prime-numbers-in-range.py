class Solution(object):
    sieve = [True] * (10 ** 6 + 1)
    sieve[1] = False
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
        prev = -1
        closest = [-1, -1]
        min_diff = float('inf')

        for i in range(left, right + 1):
            if self.sieve[i]:
                if prev != -1:
                    diff = i - prev
                    if diff < min_diff:
                        min_diff = diff
                        closest = [prev, i]
                prev = i
        
        return closest