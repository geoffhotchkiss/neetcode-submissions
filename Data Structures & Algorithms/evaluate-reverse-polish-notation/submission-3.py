"""
["4","13","5","/","+"]

stack = 4 13 5; /; --> 13/5 = 2 --> stack = 4 2
stack = 4 2; +; --> 4+2 = 6 --> stack = 6
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = set(["+", "-", "*", "/"])

        for t in tokens:
            if t in ops:
                right = stack.pop()
                left = stack.pop()
                result = None

                if t == "+":
                    result = left + right

                if t == "-":
                    result = left - right

                if t == "*":
                    result = left * right
                
                if t == "/":
                    result = left / right

                stack.append(int(result))
            
            else:
                stack.append(int(t))

        return stack[0]
            