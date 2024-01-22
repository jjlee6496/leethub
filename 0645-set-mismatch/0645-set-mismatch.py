class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check = [False]*(len(nums)+1)
        ans = [0, 0]

        for num in nums:
            if not check[num]:
                check[num] = 1
            else:
                ans[0] = num
        
        for i in range(1, len(nums)+1):
            if check[i] == 0:
                ans[1] = i
                
        return ans
                