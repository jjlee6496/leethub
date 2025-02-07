class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        stat = {}
        cnt = Counter()
        res = []
        
        for ball, color in queries:
            if ball in stat:
                old = stat[ball]
                cnt[old] -= 1
                if cnt[old] == 0:
                    del cnt[old]
            
            stat[ball] = color
            cnt[color] += 1
            res.append(len(cnt))
        return res