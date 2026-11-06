class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        i = 0
        j = n

        for m in range(n):
            result.append(nums[i])
            result.append(nums[j])
            i += 1
            j += 1

        return result


        