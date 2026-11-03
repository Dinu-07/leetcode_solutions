class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = max(nums)
        result = 0
        for i in nums:
            result += abs(data - i)
        return result        