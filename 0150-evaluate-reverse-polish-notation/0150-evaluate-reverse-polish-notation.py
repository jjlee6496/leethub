class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = set(['+', '-', '*', '/'])
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    result = num2 + num1
                elif token == '-':
                    result = num2 - num1
                elif token == '*':
                    result = num2 * num1
                elif token == '/':
                    result = num2/float(num1)

                stack.append(int(result))

        return stack.pop()