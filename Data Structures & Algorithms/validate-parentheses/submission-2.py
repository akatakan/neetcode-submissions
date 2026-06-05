class Solution:
    def isValid(self, s: str) -> bool:
        paranthesisPeer = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []

        for c in s:
            if c in paranthesisPeer.keys():
                if stack and stack[-1] == paranthesisPeer[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return False if stack else True
        
