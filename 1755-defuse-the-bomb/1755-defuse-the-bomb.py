class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        if k == 0:
            return [0] * n
        
        res = []
        for i in range(n):
            num = 0
            temp = k
            while temp != 0:
                if temp < 0:
                    num += code[(n + i + temp) % n]
                    temp += 1
                else:
                    num += code[(i + temp) % n]
                    temp -= 1
            res.append(num)
        return res