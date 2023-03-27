class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        middle = len(nums1) // 2
           
        return float(nums1[middle] + nums1[middle-1])/2 if len(nums1)%2 == 0 \
    else float(nums1[middle])
        