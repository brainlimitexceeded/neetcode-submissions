class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+','-','*','/'}
        stack = []
        for t in tokens:
            if t in ops:
                right = stack.pop(-1)
                left = stack.pop(-1)
                if t == '/':
                    ans = int(left/right)
                elif t == '*':
                    ans = left*right
                elif t == '+':
                    ans = left+right
                elif t == '-':
                    ans = left-right
                stack.append(ans)
            else:
                stack.append(int(t))
            # print(stack)
        return stack.pop(-1)