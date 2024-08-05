class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        dic = Counter(arr)
        res = []
        for c in arr:
            if dic[c] > 1:
                continue
            res.append(c)

        if k > len(res):
            return ''
        return res[k - 1]
