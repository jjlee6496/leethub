class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n=len(word1)
        m=len(word2)
        answer = ''
        for i in range(min(n,m)):
                answer += (word1[i]+word2[i])
        if n>m:
            return answer + word1[m:]
        elif n<m:
            return answer + word2[n:]
        else:
            return answer
