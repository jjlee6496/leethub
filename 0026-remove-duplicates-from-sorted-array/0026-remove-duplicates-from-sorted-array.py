class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        
        for i in range(1, len(nums)):
            current = nums[p]
            if current != nums[i]:
                p += 1
                nums[p] = nums[i]
        return p+1