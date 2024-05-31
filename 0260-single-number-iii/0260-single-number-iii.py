class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for num in nums:
            x ^= num
        
        lowest = x & -x
        res = [0, 0]
        for num in nums:
            if lowest & num:
                res[0] ^= num
            else:
                res[1] ^= num
        return res