class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        return self.merge(self.sortArray(left), self.sortArray(right))

    def merge(self, left, right):
        sorted_arr = []
        while left and right:
            if left[0] > right[0]:
                sorted_arr.append(right.pop(0))
            else:
                sorted_arr.append(left.pop(0))
        
        return sorted_arr + left + right


