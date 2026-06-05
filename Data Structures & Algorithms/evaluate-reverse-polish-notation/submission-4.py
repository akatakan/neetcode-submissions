class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "*/+-":
                num_two = stack.pop()
                num_one = stack.pop()
                operator = token
                stack.append(int(eval(f"({num_one} {operator} {num_two})")))
            else:
                stack.append(token)
        return int(stack.pop())