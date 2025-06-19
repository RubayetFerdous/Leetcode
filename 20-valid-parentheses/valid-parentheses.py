class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        dict1={")":"(","}":"{","]":"["}

        for char in s:

            if char in dict1:
                top=stack.pop() if stack else "#"
                if top!=dict1[char]: return False

            else: stack.append(char)

        return not stack

            