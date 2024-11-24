class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        prev = nums[0]
        for i in range(1, len(nums)):
            nums[i] ^= prev
            prev = nums[i]
        
        n = 2 ** maximumBit - 1
        ans = []
        for num in reversed(nums):
            ans.append(n ^ num)
        return ans