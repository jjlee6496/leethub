class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = [num for num in nums if num>=0]
        negative = [num for num in nums if num<0]
        ans = []
        for p, n in zip(positive, negative):
            ans.append(p)
            ans.append(n)
        return ans