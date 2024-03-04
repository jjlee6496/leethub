class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        return self.increasing(nums) or self.decreasing(nums)
        
    def decreasing(self, nums):
        prev = 10**5
        for num in nums:
            if prev >= num:
                prev = num
            else:
                return False
        return True

    def increasing(self, nums):
        prev = -10**5
        for num in nums:
            if prev <= num:
                prev = num
            else:
                return False
        return True