class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        result = 0
        seq = 1
        prev = colors[0]
        
        for i in range(1, n + k - 1):
            index = i % n

            if colors[index] == prev:
                seq = 1
                prev = colors[index]
            
            else:
                seq += 1
                if seq >= k:
                    result += 1
                prev = colors[index]
        return result