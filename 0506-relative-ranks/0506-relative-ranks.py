class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        h = []
        for i, s in enumerate(score):
            heappush(h, (-s, i))

        res = [0] * len(score)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        r = 1
        while h:
            pos = heappop(h)[1]
            if r<=3:
                res[pos] = rank[r-1]
            else:
                res[pos] = str(r)
            r += 1
        return res

