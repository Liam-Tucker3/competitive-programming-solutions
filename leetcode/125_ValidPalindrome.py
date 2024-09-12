class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for ch in s.lower():
            if ch in "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": newS += ch
        for i in range(int(len(newS) / 2)):
            if newS[i] != newS[len(newS) - i - 1]: return False
        return True
        