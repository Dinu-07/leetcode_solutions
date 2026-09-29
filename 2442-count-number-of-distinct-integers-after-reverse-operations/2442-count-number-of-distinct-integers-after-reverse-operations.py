class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_ = nums[:]
        for i in list_:
            rev = 0
            while (i>0):
                r =  i % 10
                rev = r + rev *10
                i//=10
            nums.append(rev)
        result = set(nums)
        return len(result)

        