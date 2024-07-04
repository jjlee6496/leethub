class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dic = set(dictionary)
    
        ans = ""
        for word in sentence.split():
            temp = ""
            flag = True
            for w in word:
                temp += w
                if temp in dic:
                    flag = False
                    ans += temp + " "
                    break
            if flag:
                ans += word + " "
        return ans.strip()