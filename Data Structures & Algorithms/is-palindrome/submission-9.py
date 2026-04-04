class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 1:
            return True

        clean = "".join(char for char in s if char.isalnum())
        l, r = 0, len(clean) - 1
        while l < r:
            if clean[l].lower() != clean[r].lower():
                return False
            l, r = l+1, r-1
        return True