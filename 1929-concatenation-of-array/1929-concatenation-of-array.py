class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:

        size = len(nums)

        for i in range(size):
            nums.append(nums[i])

        return nums

        
        