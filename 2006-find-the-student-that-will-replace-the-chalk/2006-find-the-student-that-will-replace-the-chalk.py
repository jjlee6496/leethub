class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        k %= sum(chalk)
        prefix_sum = [0] * (len(chalk) + 1)
        for i in range(1, len(chalk)+1):
            prefix_sum[i] = prefix_sum[i - 1] + chalk[i - 1]
        
        l, r = 0, len(chalk)
        while l < r:
            mid = l + ((r - l) // 2)

            if prefix_sum[mid] <= k:
                l = mid + 1
            else:
                r = mid
        return l - 1