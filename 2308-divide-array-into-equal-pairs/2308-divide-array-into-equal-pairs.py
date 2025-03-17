class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = Counter(nums)
        for v in cnt.values():
            if v % 2:
                return False
        return True