class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        return [original[i:i+n] for i in range(0, len(original) , n)] if m * n == len(original) else []