class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # nums = deque([x for x in range(1, n+1)])
        # ind = 1
        # while len(nums) > 1:
        #     for _ in range(k-1):
        #         nums.append(nums.popleft())
        #     nums.popleft()
        # return nums[0]
    #     return self.helper(n, k) + 1
    # def helper(self, n, k):
    #     if n == 1:
    #         return 0
    #     return (self.helper(n - 1, k) + k) % n
        ind = 0
        for i in range(1, n+1):
            ind = (ind + k) % i
        return ind + 1