class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cp = False
        n = len(nums)
        for i in range(1, n + 1):
            if nums[(i - 1 + n) % n] > nums[(i + n) % n]:
                if cp:
                    return False
                cp = True
        
        return True