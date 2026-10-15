class Solution:
    def isHappy(self, n: int) -> bool:
        list_ = []
        
        while(n != 1):
            if n in list_:
                return False
            list_.append(n)
            total = 0
            while(n>0):
                total += (n%10) **2
                n//=10
            n = total
            
        return True
            

        