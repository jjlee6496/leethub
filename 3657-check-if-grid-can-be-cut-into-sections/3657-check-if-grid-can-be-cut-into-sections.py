class Solution(object):
    def slicing(self, l):
        cnt = 0
        prev = l[0]
        for i in range(1, len(l)):
            if l[i][0] >= prev[1]:
                cnt += 1
                prev = l[i]
            else:
                prev = (prev[0], max(prev[1], l[i][1]))
        return cnt >= 2

    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        x = sorted([(r[0], r[2]) for r in rectangles])
        y = sorted([(r[1], r[3]) for r in rectangles])

        a = self.slicing(x)
        b = self.slicing(y)        
        return a or b