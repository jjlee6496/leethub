class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 2:
            return [1]*(rowIndex+1)
        mem = [[1,1], []]
        for i in range(1, rowIndex):
            mem[1] = [1]
            for j in range(1, i+1):
                mem[1].append(mem[0][j]+mem[0][j-1])
            mem[1].append(1)
            mem[0] = mem[1]
        return mem[0]