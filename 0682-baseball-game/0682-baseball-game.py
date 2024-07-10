class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        rec = []
        for op in operations:
            if op == 'C':
                rec.pop()
            elif op == 'D':
                rec.append(rec[-1]*2)
            elif op == '+':
                rec.append(rec[-2] + rec[-1])
            else:
                rec.append(int(op))
        return sum(rec)
