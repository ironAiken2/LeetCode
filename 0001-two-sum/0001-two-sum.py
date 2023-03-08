class Solution(object):
    def twoSum(self, nums, target):
        ii = 0
        jj = 1
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                
                if sum == target:
                    return i, j
                else:
                    ii = i
                    jj = j
                    
        return ii, jj