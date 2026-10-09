class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        j = 1
        i = 0
        while (i<len(nums)):
            if nums[i]+nums[j]==target:
                return i,j
            else:
                j+=1
                if j == len(nums):
                    i+=1
                    j = i+1
        
        