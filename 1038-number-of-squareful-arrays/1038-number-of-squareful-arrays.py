class Solution(object):
    def numSquarefulPerms(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        def squareful(a, b):
            temp = a + b
            n = int(math.sqrt(temp))
            return n*n == temp

        def dfs(perm, last, cnt):
            if len(perm) == len(nums):
                self.count += 1
                return
            
            for num in cnt:
                if cnt[num] > 0:
                    if last is not None and not squareful(last, num):
                        continue
                    cnt[num] -= 1
                    dfs(perm + [num], num, cnt)
                    cnt[num] += 1

        cnt = Counter(nums)
        self.count = 0
        dfs([], None, cnt)
        return self.count