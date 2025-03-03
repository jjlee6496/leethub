class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left, right = [], []
        cnt = 0
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                cnt += 1
            else:
                right.append(num)
        return left + [pivot]*cnt + right