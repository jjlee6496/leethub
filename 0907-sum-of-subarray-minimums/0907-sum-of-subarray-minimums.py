class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        MOD = 1000000007
        ans = 0
        n = len(arr)

        for i in range(n+1):
            while stack and (i==n or arr[stack[-1]] >= arr[i]):
                ind = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                cnt = (ind - left)*(right - ind)
                ans += cnt*arr[ind] % MOD
            stack.append(i)
        return ans% MOD