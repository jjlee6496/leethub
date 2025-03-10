class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        colors = colors + colors[:k - 1]
        n = len(colors)
        res = 0
        l = 0
        r = 1
        while r < n:
            if colors[r] == colors[r - 1]:
                l = r
                r += 1
            
            else:
                r += 1
                if r - l == k:
                    res += 1
                    l += 1
        return res
