class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        n = len(str(low))
        m = len(str(high))

        res = []
        while n <= m:
            for i in range(1, 9-n+2):
                answer = ''
                for _ in range(n):
                    answer += str(i)
                    i+=1
                if low<=int(answer)<=high:
                    res.append(int(answer))
                
            n += 1
        return res

        