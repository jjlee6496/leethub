class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        cnt = [0] * k
        for num in arr:
            cnt[num % k] += 1
        if cnt[0] % 2:
            return False
        for i in range(1, k//2 + 1):
            if cnt[i] != cnt[k - i]:
                return False
        return True