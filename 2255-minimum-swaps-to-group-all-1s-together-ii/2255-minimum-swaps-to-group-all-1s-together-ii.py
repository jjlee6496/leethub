class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k = nums.count(1) # total number of ones
        ones = max_ones = sum(nums[:k]) # init current, max ones to first k size window
        
        # k size window를 유지하면서 왼쪽은 빼주고 오른쪽은 더해줌 circular를 위해 mod n
        for i in range(k, n+k):
            ones += nums[i % n]
            ones -= nums[(i - k + n) % n]
            max_ones = max(max_ones, ones)
        return k - max_ones
