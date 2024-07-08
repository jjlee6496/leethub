class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums = deque([x for x in range(1, n+1)])
        ind = 1
        while len(nums) > 1:
            if ind == k:
                nums.popleft()
                ind = 1
            else:
                nums.append(nums.popleft())
                ind += 1
        return nums[0]
            