class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        prefix = self.getPrefixArr(self.nums)
        rt = prefix[right]
        lt = 0
        if left == 0:
            lt = 0
        else:
            lt = prefix[left-1]
        return rt-lt
    
    def getPrefixArr(self, nums: list[int]) -> list[int]:
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        
        return prefix

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)