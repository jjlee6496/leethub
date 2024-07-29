class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(rating)):
            small = [x for x in rating[:i] if x < rating[i]]
            large = [x for x in rating[i:] if x > rating[i]]
            total += len(small) * len(large)

        for i in range(len(rating)):
            large = [x for x in rating[:i] if x > rating[i]]
            small = [x for x in rating[i:] if x < rating[i]]
        
            total += len(small) * len(large)
        return total