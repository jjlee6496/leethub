class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        mem = [[1]*(i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, len(mem[i])-1):
                mem[i][j] = mem[i-1][j] + mem[i-1][j-1]
        return mem