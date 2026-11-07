class Solution:
    def mirrorDistance(self, n: int) -> int:
        m = n
        rev = 0
        while(m>0):
            r = m % 10
            rev = rev*10 + r
            m //= 10

        return abs(rev - n)