class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = {}
        list_ = []
        for i in nums:
            result[i] = result.get(i,0) + 1
        for i in result:
            if result[i] == 1:
                list_.append(i)
        return list_
        
        