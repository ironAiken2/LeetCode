class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        zero = []
        
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zero.append(0)
            else:
                i += 1
                
        nums += zero
                
                