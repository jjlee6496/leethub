class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        cnt = 0
        for log in logs:
            if log == '../':
                cnt -= 1
                cnt = max(0, cnt)
            elif log == './':
                continue
            else:
                cnt += 1
        return cnt