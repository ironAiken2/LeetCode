class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
            
        return nums