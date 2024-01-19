class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==1:
            return
        
        ind1 = -1
        ind2 = n-1
        
        for i in range(n-2, -1, -1):
            if nums[i]< nums[i+1]:
                ind1 = i
                break

        if ind1==-1:
            nums.reverse()
            return
        
        for j in range(n-1, ind1, -1):
            if nums[j]>nums[ind1]:
                ind2 = j
                break
        
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
        
        tail = ind1+1
        head = n-1
        while head > tail:
            nums[head], nums[tail] = nums[tail], nums[head]
            tail += 1
            head -= 1
            
        