class Solution:
    def majorityElement(self, nums: List[int]) -> int:        
        nums.sort()
        nums.append(None)
        
        current = nums[0]
        cnt = 1
        
        ans = 0
        max_cnt = 0
        
        for i in range(1, len(nums)):
            if nums[i] == current:
                cnt += 1
            else:
                if max_cnt <= cnt:
                    max_cnt = cnt
                    ans = current
                cnt = 1
                current = nums[i]
                    
            
        return ans
                    