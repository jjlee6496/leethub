class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        total = 0
        n = len(rating)
        for i in range(1, n-1):
            l_s = sum([rating[j] < rating[i] for j in range(i)])
            l_g = i - l_s
            r_g = sum([rating[k] > rating[i] for k in range(i+1, n)])
            r_s = n - i - 1 - r_g
            total += l_s*r_g + l_g*r_s
        return total