def isValid(s: list[str]) -> bool:
    stack = []

    if len(s) % 2 != 0:
        return False

    open = {'('}

    for i in range(len(s)):
        item = s[i]

        if item in open:
            stack.append(item)
            continue

        # close case
        pop_item = ""
        if stack:
            pop_item = stack.pop()
        if item == ')' and pop_item == '(':
            continue
        else:
            return False

    return True if len(stack) == 0 else False


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        final = []
        current_state = []

        def dfs():
            if len(current_state) == n * 2:
                result.append(current_state.copy())
                return

            current_state.append("(")
            dfs()
            current_state.pop()

            current_state.append(")")
            dfs()
            current_state.pop()

        dfs()

        for item in result:
            if isValid(item):
                final.append("".join(item))

        return final