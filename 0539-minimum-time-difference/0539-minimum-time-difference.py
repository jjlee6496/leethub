class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # [0, 1439] 범위로 정해져 있으므로 bucket sort 사용 가능
        def t2m(time):
            h, m = map(int, time.split(':'))
            return h * 60 + m
        
        times = [False] * 1440
        first_time, last_time = 1440, 0
        for time in timePoints:
            m = t2m(time)
            if times[m]:
                return 0
            times[m] = True
            first_time = min(first_time, m)
            last_time = max(last_time, m)

        res = 1440 - last_time + first_time
        prev = first_time
        for i in range(first_time + 1, last_time + 1):
            if times[i]:
                diff = i - prev
                res = min(res, diff)
                prev = i
        return res

        


