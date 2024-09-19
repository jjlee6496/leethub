class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints.sort()
        
        def t2m(time):
            h, m = map(int, time.split(':'))
            return h * 60 + m
        
        res = 1440 # 24 * 60이 최대 분
        for i in range(1, len(timePoints)):
            t1, t2 = t2m(timePoints[i - 1]), t2m(timePoints[i])
            res = min(res, t2 - t1)
        res = min(res, 1440 - t2m(timePoints[-1]) + t2m(timePoints[0]))
        return res

