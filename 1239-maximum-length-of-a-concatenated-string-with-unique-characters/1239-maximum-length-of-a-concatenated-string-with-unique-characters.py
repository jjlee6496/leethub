class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        charset = set()

        def Overlap(charset, string):
            c = Counter(charset)+Counter(string)
            return max(c.values()) > 1
        temp = set()
        # for s in string:
        #     if s in temp or s in charset:
        #         return True
        #     s.add(s)
        # return False
        
        def backtrack(index):
            if index == len(arr):
                return len(charset)
            res = 0
            if not Overlap(charset, arr[index]):
                for c in arr[index]:
                    charset.add(c)
                res = backtrack(index+1)
                for c in arr[index]:
                    charset.remove(c)
            return max(res, backtrack(index+1))
        return backtrack(0)


