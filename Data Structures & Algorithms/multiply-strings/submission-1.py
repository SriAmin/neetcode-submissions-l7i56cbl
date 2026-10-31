class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hashSet = { "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
        nArr1, nArr2 = [], []
        n1, n2 = 0, 0
        
        for n in num1:
            nArr1.append(hashSet[n])
        for n in num2:
            nArr2.append(hashSet[n])

        for digit in nArr1:
            n1 = n1 * 10 + digit
        for digit in nArr2:
            n2 = n2 * 10 + digit

        return str(n1 * n2)
