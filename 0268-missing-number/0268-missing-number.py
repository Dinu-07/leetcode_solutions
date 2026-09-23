class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = set(nums)
        for i in range(len(result)+1):
            if i not in result:
                return i
            

        