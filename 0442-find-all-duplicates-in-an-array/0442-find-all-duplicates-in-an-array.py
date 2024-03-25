class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 2:
            return []
        
        ans = []
        check = [0] * (n + 1)

        for num in nums:
            if not check[num]:
                check[num] = 1
            elif check[num]:
                ans.append(num)
        return ans