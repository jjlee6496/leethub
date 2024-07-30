class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0
        b_cnt = 0
        for a in s:
            if a == 'a':
                deletions = min(deletions + 1, b_cnt)
            else:
                b_cnt += 1
        return deletions

