class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        k = len(nums)
        for i in range(1,k+1):
            if k % i == 0:
                result = result +  nums[i-1]**2
        return result
        