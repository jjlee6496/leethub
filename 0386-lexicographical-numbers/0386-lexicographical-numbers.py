class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = [str(i) for i in range(1, n+1)]
        return list(map(int, sorted(nums)))
        