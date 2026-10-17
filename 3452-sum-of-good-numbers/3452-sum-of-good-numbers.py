class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            if i-k >=0 and nums[i] <= nums[i-k]:
                continue
            if i+k < len(nums) and nums[i] <= nums[i+k]:
                continue
            result += nums[i]
        return result
                    
        