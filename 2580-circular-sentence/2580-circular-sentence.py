class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        sentence = sentence.split()

        n = len(sentence)
        if n == 1:
            return sentence[0][0] == sentence[0][-1]

        for i in range(1, n):
            if sentence[i - 1][-1] != sentence[i][0]:
                return False
        
        return sentence[0][0] == sentence[-1][-1]