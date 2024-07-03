class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        res = [1]
        prev = 1
        for k in range(1, rowIndex + 1):
            next = prev * (rowIndex - k + 1) / k
            res.append(next)
            prev = next
        return res
