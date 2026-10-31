class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 2
        while(i <= n-2):
            list_ = []
            num = n
            while (num > 0):
                list_.append(str(num%i))
                num //= i
            listt = list_[:]
            str2 = ''.join(listt)
           
            str1 = ''.join(reversed(list_))
           
            if int(str1) == int(str2):
                i+=1
               
            else:
                return False
        return True
        

            