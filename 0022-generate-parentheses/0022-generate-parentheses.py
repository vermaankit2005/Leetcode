class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        final = []
        current_state = []

        def dfs(open_count, close_count):
            if len(current_state) == n * 2:
                result.append(current_state.copy())
                return
            
            if open_count < n:
                current_state.append("(")
                open_count += 1
                dfs(open_count, close_count)
                current_state.pop()
                open_count -= 1

            if close_count < open_count:
                current_state.append(")")
                close_count += 1
                dfs(open_count, close_count)
                current_state.pop()
                close_count -= 1

        dfs(0, 0)

        for item in result:
            final.append("".join(item))

        return final