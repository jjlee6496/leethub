class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(rating)):
            l_s,  r_g,  l_g,  r_s = 0, 0, 0, 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    l_s += 1
                else:
                    l_g += 1

            for k in range(i+1, len(rating)):
                if rating[k] < rating[i]:
                    r_s += 1
                else:
                    r_g += 1
            total += l_s * r_g + l_g * r_s
        return total