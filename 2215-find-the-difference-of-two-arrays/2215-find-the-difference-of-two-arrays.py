class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        l = []
        l.append(list(s1-s2))
        l.append(list(s2-s1))
        return l
        