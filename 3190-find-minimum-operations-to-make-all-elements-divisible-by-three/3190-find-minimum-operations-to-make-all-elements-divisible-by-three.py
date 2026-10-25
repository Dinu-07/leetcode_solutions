class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            if i % 3 == 0:
                pass
            elif (i+1) % 3 == 0 or (i-1)%3 == 0:
                result += 1
            else:
                pass
        return result
        