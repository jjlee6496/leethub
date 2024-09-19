class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
        }

        def dfs(left, right):
            res = []
            for i in range(left, right + 1):
                op = expression[i]
                if op in ops:
                    nums1 = dfs(left, i - 1)
                    nums2 = dfs(i + 1, right)
                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(ops[op](n1, n2))
            # Base case: 숫자만 있음
            if res == []:
                res.append(int(expression[left:right+1]))
            return res

        return dfs(0, len(expression) - 1)