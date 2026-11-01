class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        list_ = []
        for i in range(n):
            list_.append(nums[i])
            list_.append(nums[i+n])
        return list_
        