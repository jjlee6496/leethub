class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        temp = [s[i:i+k] for i in range(0, len(s), k)]
        if len(temp[-1]) % k:
            temp[-1] += fill*(k - (len(temp[-1]) % k))
        return temp