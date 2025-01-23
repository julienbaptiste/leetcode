class Solution(object):
    def isPalindrome(self, x):
        return False if x < 0 else (str(x) == str(x)[::-1])