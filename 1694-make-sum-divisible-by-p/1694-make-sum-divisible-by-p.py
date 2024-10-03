class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        n = len(nums)
        target = sum(nums) % p
        if target == 0:
            return 0
        prefix = 0
        min_length = n
        seen = {0: -1}
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            complement = (prefix - target) % p
            if complement in seen:
                min_length = min(min_length,  i - seen[complement])
            seen[prefix] = i
        return min_length if min_length < n else -1
        

