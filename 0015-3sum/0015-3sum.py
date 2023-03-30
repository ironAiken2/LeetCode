class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dup = set()
        nums.sort()
        
        for i in range(len(nums)-2):
            end = len(nums)-1
            mid = i+1
            
            while mid < end:
                sum3 = nums[i] + nums[mid] + nums[end]
                
                if sum3 == 0:
                    dup.add((nums[i], nums[mid], nums[end]))
                    mid += 1
                    end -= 1
                elif sum3 < 0:
                    mid += 1
                else:
                    end -= 1
                    
        dup = list(dup)
        
        return dup