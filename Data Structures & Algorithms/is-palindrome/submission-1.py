class Solution:
    def isPalindrome(self, s: str) -> bool:
        NS=''
        for c in s:
            if c.isalnum():
                NS += c.lower()
        return NS==NS[::-1]