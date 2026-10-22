class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for i in nums:
            result[i] = result.get(i,0) + 1
        for freq in result:
            if result[freq] == 1:
                return freq