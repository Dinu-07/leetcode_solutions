class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        list_ = []
        list1 = []
        count = 0
        for i in nums:
            if i < pivot:
                list_.append(i)
            elif i > pivot:
                list1.append(i)
            else:
                count+=1
        for i in range(count):
            list_.append(pivot)
        list_.extend(list1)
        return list_
        