class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        arr = []
        ops = set('+-*')
        num = 0
        for e in expression:
            if e in ops:
                arr.append(num)
                num = 0
                arr.append(e)
            else:
                num = num * 10 + int(e)
        arr.append(num)


        def dfs(left, right):
            if left == right:
                return [arr[left]]

            res = []
            for i in range(left, right):
                op = arr[i]
                if op in ops:
                    nums1 = dfs(left, i - 1)
                    nums2 = dfs(i + 1, right)
                    
                    if op == '+':
                        for n1 in nums1:
                            for n2 in nums2:
                                res.append(n1 + n2)
                    elif op == '-':
                        for n1 in nums1:
                            for n2 in nums2:
                                res.append(n1 - n2)
                    elif op == '*':
                        for n1 in nums1:
                            for n2 in nums2:
                                res.append(n1 * n2)
            return res

        return dfs(0, len(arr) - 1)