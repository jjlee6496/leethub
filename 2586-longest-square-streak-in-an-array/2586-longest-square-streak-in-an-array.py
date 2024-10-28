class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = 10 ** 5
        hashset = set(nums)
        res = -1
        for num in nums:
            cnt = 1
            while num <= MAX:
                if num * num in hashset:
                    cnt += 1
                    num = num * num
                else:
                    break
            if cnt >= 2:
                res = max(res, cnt)
        return res