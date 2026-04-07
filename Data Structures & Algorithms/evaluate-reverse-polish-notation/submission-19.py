class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(["+", "-", "*", "/"])
        for t in tokens:
            if t in operations:
                val1 = stack.pop()
                val2 = stack.pop()
                if t == "+":
                    stack.append(val1 + val2)
                elif t == "*":
                    stack.append(val1 * val2)
                elif t == "-":
                    stack.append(val2 - val1)
                elif t == "/":
                    stack.append(int(val2 / val1))
            else:
                stack.append(int(t))
        return stack.pop()