class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
       nums1.extend(nums2)
       nums1.sort()
       size = len(nums1)
       if size%2 == 0:
        a = nums1[size//2 - 1]
        b =  nums1[size//2]
        return (a+b)/2
       else:
        return nums1[size//2]
        