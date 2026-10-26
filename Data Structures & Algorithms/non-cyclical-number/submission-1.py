class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            digits = [int(d) for d in str(n)]
            sum = 0
            for d in digits:
                sum += d ** 2
            return sum

        hashSet = set()
        while n not in hashSet:
            hashSet.add(n)
            n = getSum(n)
            if n == 1:
                return True
        return False