class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        f, l = strs[0], strs[-1]
        res = ""
        for i in range(len(f)):
            if f[i] != l[i]:
                return res
            res += f[i]
        return res