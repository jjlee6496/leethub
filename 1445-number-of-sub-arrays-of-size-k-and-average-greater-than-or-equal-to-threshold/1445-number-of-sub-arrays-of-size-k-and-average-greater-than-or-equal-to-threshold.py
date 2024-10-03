class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = 0 
        L, curr = 0, 0
        for R in range(len(arr)):
            curr += arr[R]
            if R - L + 1 > k:
                curr -= arr[L]
                L += 1
            if R - L + 1 == k and curr >= threshold * k:
                res += 1
            
        return res