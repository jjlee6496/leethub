class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = 0
        n = len(arr)
        curr = sum(arr[:k])
        if curr >= threshold * k:
            res += 1
        for i in range(n - k):
            curr += (arr[i + k] - arr[i])
            if curr >= threshold * k:
                res += 1
        return res