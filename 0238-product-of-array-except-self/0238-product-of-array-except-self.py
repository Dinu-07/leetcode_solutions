class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero = 0
        total = 1
        for i in nums:
            if i == 0:
                zero +=1
            else :
                total *= i
        if zero >1:
            result = [0 *x for x in nums]
        elif zero == 1:
            result = [0 if x!=0 else total for x in nums]
        else:
            result = [total / x for x in nums]
        return result



       