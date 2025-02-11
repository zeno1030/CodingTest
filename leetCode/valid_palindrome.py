import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        s = re.sub(r'[^0-9a-zA-Z]', '', s)
        s = s.lower()
        reverse_s = s[::-1]

        if s == reverse_s:
            return True
        else:
            return False
