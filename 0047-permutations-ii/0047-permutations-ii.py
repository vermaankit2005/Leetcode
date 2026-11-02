class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        used = [False] * len(nums)
        seen = set()

        def traverse(i: int, current_state: list[int]):

            if len(current_state) == len(nums):
                if tuple(current_state) in seen:
                    return

                ans.append(current_state.copy())
                seen.add(tuple(current_state))
                return

            for j in range(len(nums)):

                if used[j]:
                    continue

                used[j] = True
                current_state.append(nums[j])

                traverse(i + 1, current_state)

                current_state.pop()
                used[j] = False

        traverse(0, [])
        return ans
        