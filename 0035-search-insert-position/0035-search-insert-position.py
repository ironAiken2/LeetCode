class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        start = 0
        end = len(nums) - 1
        
        while end - start > 0:
            index = int((start+end)/2)
            
            if nums[index] < target:
                start = index + 1
            else:
                end = index
                
        
        return start