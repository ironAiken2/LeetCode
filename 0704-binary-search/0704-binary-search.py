class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        ans = 0
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] <= target:
                left = middle + 1
                ans = middle
            else:
                right = middle - 1
                
        return ans if nums[ans] == target else -1