class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        result = 0
        for i in str(n):
            result = result + int(i)
        return result

        