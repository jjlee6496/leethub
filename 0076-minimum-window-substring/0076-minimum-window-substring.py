class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == '':
            return ''
        window, dic = defaultdict(int), defaultdict(int)
        res, resLen = [-1, -1], float('inf') # pointer[l, r]
        l = 0

        # t 해시맵 생성
        for c in t:
            dic[c] += 1
        
        have, need = 0, len(dic)
        
        # s 하나씩 보면서
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in dic and window[c] == dic[c]:
                have += 1

            while have == need:
                # update
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of current window
                window[s[l]] -= 1
                # 만약 필요한 글자를 부족하도록 없앴다면
                if s[l] in dic and window[s[l]] < dic[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ''