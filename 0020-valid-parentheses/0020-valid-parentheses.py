class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s)%2 != 0:
            return False

        open = set(['(' , '[', '{'])

        for i in range(len(s)):
            item = s[i]
            
            if item in open: 
                stack.append(item)
                continue
            
            # close case
            pop_item = ""
            if stack: 
                pop_item = stack.pop()
            if (item == ')' and pop_item == '(') or (item == ']' and pop_item == '[') or (item == '}' and pop_item == '{'):
                continue
            else:
                return False
            
        return True if len(stack) == 0 else False
            
        