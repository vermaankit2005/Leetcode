class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        prefix = []
        postfix = deque()
        result = []
        prepro = 1
        postpro = 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1 , -1)):

            prepro *= nums[i]
            postpro *= nums[j]

            prefix.append(prepro)
            postfix.appendleft(postpro)
        
        for i in range(len(nums)):
            leftpro = 1
            rightpro = 1
            if i > 0:
                leftpro = prefix[i-1]
            if i < len(nums)-1:
                rightpro = postfix[i+1]
            
            result.append(leftpro*rightpro)

            
        return result
                

        