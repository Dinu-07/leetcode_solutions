class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_ = set(nums)
        result = []
        for i in range(1,len(nums)+1):
            if i not in list_:
                result.append(i)
        return result


        