class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        pre_fix = []
        post_fix = deque()

        pre_sum = 0
        post_sum = 0
        result = float('inf')
        
        for i, j in zip(range(len(nums)), range(len(nums)-1 , -1 , -1)):
            pre_sum += nums[i]
            post_sum += nums[j]

            pre_fix.append(pre_sum)
            post_fix.appendleft(post_sum)

        for i in range(len(pre_fix)):
            if pre_fix[i] == post_fix[i]:
                return i
        
        return -1


            

            



        