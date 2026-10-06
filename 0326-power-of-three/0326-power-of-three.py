import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n>0:
            x = math.log(n,3)
            x = round(x)
            return (3**x) == n
        return False
        
        