class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = len(nums)//2
        mid = nums[i]
        result = 0
        for element in nums:
            result += abs(mid - element)
        return result
        