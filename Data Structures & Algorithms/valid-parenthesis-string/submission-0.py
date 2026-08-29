class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack, starStack = [], []

        for i in range(len(s)):
            if s[i] == "(":
                leftStack.append(i)
            if s[i] == "*":
                starStack.append(i)
            if s[i] == ")":
                if len(leftStack) >= 1:
                    leftStack.pop()
                elif len(starStack) >= 1:
                    starStack.pop()
                else:
                    return False
        print(leftStack)
        print(starStack)
        while len(leftStack) >= 1 and len(starStack) >= 1:
            iL = leftStack.pop()
            iS = starStack.pop()
            if iL > iS:
                return False
        return len(leftStack) == 0