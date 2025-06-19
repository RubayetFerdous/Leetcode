class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        for i in s:
            if i.isalnum(): n+=i

        n=n.lower()

        for i in range(len(n)):
            if n[i]!=n[len(n)-i-1]: return False

        return True