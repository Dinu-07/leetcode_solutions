class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_ = [i*i for i in nums]
        list_.sort()
        return list_
        