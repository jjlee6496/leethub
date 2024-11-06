class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        changed = True
        while changed:
            changed = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    if self.count_bits(nums[i]) == self.count_bits(nums[i + 1]):
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        changed = True
                    else:
                        return False
        return True
    def count_bits(self, num):
        cnt = 0
        while num:
            cnt += num & 1
            num >>= 1
        return cnt