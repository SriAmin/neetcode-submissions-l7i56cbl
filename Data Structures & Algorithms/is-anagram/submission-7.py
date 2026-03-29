class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str1, str2 = {}, {}
        
        for i in s:
            str1[i] = str1[i] + 1 if i in str1 else 1
        for j in t:
            str2[j] = str2[j] + 1 if j in str2 else 1

        return str1 == str2
 