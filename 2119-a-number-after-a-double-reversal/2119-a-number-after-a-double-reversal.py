class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        i = 0
        while (i<2):
             rev = 0
             while(num>0):
                r = num%10
                rev = r + rev * 10
                num = num // 10
             num = rev
             i+=1
        
        return rev == x 



        