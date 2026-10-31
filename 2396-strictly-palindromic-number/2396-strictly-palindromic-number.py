class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(2, n-1):
            num = n
            s = ""
            while(num > 0):
                s += str(num % i)
                num //= i
            if s != s[::-1]:
                return False
        return True
        
       
        

            