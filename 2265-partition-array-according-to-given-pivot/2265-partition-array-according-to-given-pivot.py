class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left, mid, right = [], [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)
        return left + mid + right