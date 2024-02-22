class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        
        for a, b in trust:
            outgoing[a] += 1
            incoming[b] += 1

        for i in range(1, n+1):
            if outgoing[i] == 0 and incoming[i] == (n-1):
                return i
        return -1 