class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = i
        
        for i in range(len(nums)):
            no_to_look = target - nums[i]
            if(no_to_look in maps and i != maps[no_to_look]):
                return[i , maps[no_to_look]]
        return []

        