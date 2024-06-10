class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        return sum([heights[i]!=expected[i] for i in range(len(heights))])