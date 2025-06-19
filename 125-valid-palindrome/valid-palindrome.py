class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j=0, len(s)-1

        while i<j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()!=s[j].lower(): return False
                else: 
                    i+=1
                    j-=1
            elif s[i].isalnum() and not s[j].isalnum(): j-=1
            elif s[j].isalnum() and not s[i].isalnum(): i+=1
            else:
                i+=1
                j-=1

        return True
                
