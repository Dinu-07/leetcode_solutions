class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        list_ = sorted(set(x for x in nums if x%2 == 0))
        result = -1
        max_count = 0
        for i in list_:
            if max_count < nums.count(i):
                max_count = nums.count(i)
                result = i
        return result
        