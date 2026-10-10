class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        if (len(nums)) < 3:
            return nums
        list_1 = [nums[x] for x in range(len(nums)) if x%2==0]
        list_2 = [nums[i] for i in range(len(nums)) if i%2 !=0]
        list_1.sort()
        list_2.sort(reverse = True)
        list_ = []
        i = 0
        while i < len(list_1) or i<len(list_2):
            if i<len(list_1):
                list_.append(list_1[i])
            if i<len(list_2):
                list_.append(list_2[i])
            i+=1
        return list_

        