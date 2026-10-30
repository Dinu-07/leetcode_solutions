class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        low = [x for x in nums  if x<pivot]
        high =[x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        return low+mid+high
        