class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = []
        temp = [nums[0]]
        prev = self.count_bits(nums[0])
        for i in range(1, len(nums)):
            cnt = self.count_bits(nums[i])
            if cnt == prev:
                temp.append(nums[i])
            else:
                arr.append(temp)
                temp = [nums[i]]
                prev = cnt
        arr.append(temp)
        
        for i in range(1, len(arr)):
            if max(arr[i - 1]) > min(arr[i]):
                return False
        return True

    def count_bits(self, num):
        cnt = 0
        while num:
            num &= (num - 1)
            cnt += 1
        return cnt