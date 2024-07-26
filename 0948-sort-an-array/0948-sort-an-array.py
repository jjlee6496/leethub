class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bucket = [0] * 100001
        for x in nums:
            bucket[x+50000] += 1
        ans = []
        for i, x in enumerate(bucket, -50000):
            ans.extend([i] * x)
        return ans