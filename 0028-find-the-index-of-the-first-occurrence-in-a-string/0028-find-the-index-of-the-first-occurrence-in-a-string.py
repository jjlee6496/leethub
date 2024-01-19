class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lps = [0]*len(needle)
        pre = 0

        for i in range(1, len(needle)):
            while pre>0 and needle[i] != needle[pre]:
                pre = lps[pre-1]

            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre
        
        n_ptr = 0
        for h_ptr in range(len(haystack)):
            while n_ptr>0 and haystack[h_ptr] != needle[n_ptr]:
                n_ptr = lps[n_ptr-1]
            
            if haystack[h_ptr] == needle[n_ptr]:
                n_ptr += 1
            if n_ptr == len(needle): # 글자가 완성되면
                return h_ptr - n_ptr + 1 # 첫 인덱스 반환
        return -1
