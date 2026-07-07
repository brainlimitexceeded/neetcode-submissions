class Solution:
    def isValid(self, s: str) -> bool:
        open = {'[','{','('}
        close = {']','}',')'}
        maps = dict()
        maps.update({')':'('})
        maps.update({']':'['})
        maps.update({'}':'{'})
        stack=[]
        for ss in s:
            if ss in open:
                stack.append(ss)
            else:
                if len(stack)<1 or stack[-1] != maps.get(ss):
                    return False
                stack.pop(-1)
        return True if len(stack) == 0 else False