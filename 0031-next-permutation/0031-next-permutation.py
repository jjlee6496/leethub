class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==1:
            return
        
        ind = -1
        
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break
        
        if ind == -1:
            nums.reverse()
            return
        
        for j in range(n-1, ind, -1):
            if nums[ind] < nums[j]:
                nums[ind], nums[j] = nums[j], nums[ind]
                break
        nums[ind+1:] = reversed(nums[ind+1:])
        return
        