class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        cnt = [0 for _ in range(26)]
        for i in words[0]:
            cnt[ord(i) - ord('a')] += 1
        
        for word in words[1:]:
            temp = [0 for _ in range(26)]
            for j in word:
                temp[ord(j) - ord('a')] += 1
            for k in range(26):
                cnt[k] = min(cnt[k], temp[k])
        for i in range(26):
            if cnt[i]:
                for _ in range(cnt[i]):
                    res.append(chr(i + ord('a')))
        return res