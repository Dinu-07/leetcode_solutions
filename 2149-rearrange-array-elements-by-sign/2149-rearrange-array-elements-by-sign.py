class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        list_ = []
        list_1 = [x for x in nums if x > 0]
        list_2 = [x for x in nums if x < 0]
        for i in range(len(list_1)):
            list_.append(list_1[i])
            list_.append(list_2[i])
        return list_
