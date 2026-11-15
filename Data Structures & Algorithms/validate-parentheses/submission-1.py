class Solution:
    def isValid(self, s: str) -> bool:
        # push both of it in there
        stack = []
        totalList = {"}": "{", "]": "[", ")": "("}
        
        for i in range(0, len(s)):
            v = s[i]
            if v in totalList:
                if stack and stack[-1] == totalList[v]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(v)
                # you make sure you clear everything 
        return True if not stack else False

        