class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        list_ = [x for x in nums if x%2 == 0]
        result = {}
        for i in list_:
            result[i] = result.get(i,0)+1
        max_count = 0
        ans = -1
        for num,freq in result.items():
            if max_count<freq:
                max_count = freq
                ans = num
            elif freq == max_count and num<ans:
                ans = num
        return ans

        