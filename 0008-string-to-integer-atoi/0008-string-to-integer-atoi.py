class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()  # 앞뒤 공백 제거
        if not s:  # 빈 문자열 처리
            return 0
        
        temp = ''
        for i, c in enumerate(s):
            if i == 0 and c in ['-', '+']:
                temp += c
            elif c.isdigit():
                temp += c
            else:
                break  # 숫자가 아닌 문자가 나오면 종료

        if temp == '' or temp in ['-', '+']:
            return 0
        
        result = int(temp)
        
        # 32-bit integer 범위로 제한
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        return result