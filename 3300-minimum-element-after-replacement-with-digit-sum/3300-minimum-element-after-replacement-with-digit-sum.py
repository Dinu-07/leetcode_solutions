class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            result = 0
            while(n>0):
                r = n % 10
                result += r
                n //= 10
            nums[i] = result
                
        return min(nums)

        