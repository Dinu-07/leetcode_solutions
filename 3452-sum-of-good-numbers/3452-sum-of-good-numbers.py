class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            j = i + k
            t = i - k
            if j < len(nums) and t >= 0:
                if nums[i] > nums[j] and nums[i] > nums[t]:
                    result += nums[i]
            elif j >= len(nums) and t >=0:
                if nums[i] > nums[t]:
                    result += nums[i]
            elif j<len(nums) and t<0:
                if nums[i]>nums[j]:
                    result += nums[i]
            else:
                pass
        return result
                    
        