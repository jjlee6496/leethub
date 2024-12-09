class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(nums)
        prefix = [0] * n
        ans = []
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + ((nums[i - 1] & 1) ^ (nums[i] & 1))

        for start, end in queries:
            if start == end:
                ans.append(True)
            else:
                expected = start - end
                actual = prefix[start] - prefix[end]
                ans.append(expected == actual)
        return ans
            
