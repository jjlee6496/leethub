class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(arr)
        l, r = 0.0, 1.0
        res = []
        p = q = 0
        while l < r:
            m = (l + r) / 2
            maxF = 0
            cnt = 0
            j = 1
            for i in range(n-1):
                while j < n and arr[i]/float(arr[j]) > m:
                    j += 1
                if j == n:
                    break
                cnt += n - j

                if arr[i]/float(arr[j]) > maxF:
                    p, q = arr[i], arr[j]
                    maxF = p / float(q)
            
            if cnt == k:
                return p, q
            if cnt < k:
                l = m
            else:
                r = m
