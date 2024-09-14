class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        res = []
        for l, r in queries:
            if l != 0:
                temp = arr[r] ^ arr[l - 1]
            else:
                temp = arr[r]
            res.append(temp)
        return res