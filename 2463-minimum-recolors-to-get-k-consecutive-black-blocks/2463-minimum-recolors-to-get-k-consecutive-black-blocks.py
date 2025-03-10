class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        white_count = blocks[:k].count('W')
        res = white_count

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white_count += 1
            if blocks[i - k] == 'W':
                white_count -= 1
            
            res = min(res, white_count)

        return res