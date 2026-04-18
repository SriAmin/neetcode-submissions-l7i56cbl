class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26
        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_s2[ord(s2[i]) - ord('a')] += 1

        l = 0
        r = len(s1) - 1
        while r < len(s2) - 1:
            if freq_s2 == freq_s1:
                return True
            r = r + 1
            freq_s2[ord(s2[l]) - ord('a')] -= 1
            freq_s2[ord(s2[r]) - ord('a')] += 1
            l = l + 1
        return freq_s2 == freq_s1

        