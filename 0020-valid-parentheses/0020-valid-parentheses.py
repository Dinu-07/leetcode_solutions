class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_ = []
        result = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in result :
                if not stack_ or stack_.pop() != result[i]:
                    return False
            else:
                stack_.append(i)
        return not stack_  

       

                    
                      

        