class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for v in Counter(nums).values():
            if v % 2:
                return False
        return True