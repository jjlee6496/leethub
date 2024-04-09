class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_n, cnt = max(nums), 0
        l = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == max_n:
                cnt += 1
            
            while cnt > k or (l < r and cnt == k and nums[l] != max_n):
                if nums[l] == max_n:
                    cnt -= 1
                l += 1
            if cnt == k:
                res += l + 1
        return res


