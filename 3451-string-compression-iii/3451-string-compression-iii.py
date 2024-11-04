class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        cnt = 1
        i = 0
        res = []
        while i < len(word):
            if i > 0 and word[i] == word[i - 1] and cnt < 9:
                cnt += 1
            elif (i > 0 and word[i] != word[i - 1]) or cnt == 9:
                res.append(str(cnt) + word[i - 1])
                cnt = 1
            i += 1
        res.append(str(cnt) + word[i - 1])
        return ''.join(res)
