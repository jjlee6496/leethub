class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res = [0]*3
        for num in nums:
            res[num] += 1
        ind = 0
        while ind < len(nums):
            for i, num in enumerate(res):
                for _ in range(num):
                    nums[ind] = i
                    ind += 1
        return nums