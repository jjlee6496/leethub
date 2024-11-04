class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        cnt = 0
        curr = word[0]
        res = []
        for w in word:
            if w == curr and cnt < 9:
                cnt += 1
            else:
                res.append(str(cnt))
                res.append(curr)
                cnt = 1
                curr = w
        res.append(str(cnt))
        res.append(curr)
        return ''.join(res)
